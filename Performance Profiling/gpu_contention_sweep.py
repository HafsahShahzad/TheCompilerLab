import numpy as np, sys, torch, time, multiprocessing as mp
import matplotlib.pyplot as plt
import pandas as pd

def now():
    return time.perf_counter()

def summarize(samples):
    import numpy as np
    s = np.array(samples)
    return {"mean_s": float(s.mean()), "min_s": float(s.min()), "max_s": float(s.max()), "std_s": float(s.std())}

def bench_sync(fn, warmup=2, iters=8, synchronize_gpu=True):
    for _ in range(warmup):
        fn()
        if synchronize_gpu and torch.backends.mps.is_available():
            torch.mps.synchronize()
    samples = []
    for _ in range(iters):
        t0 = now()
        fn()
        if synchronize_gpu and torch.backends.mps.is_available():
            torch.mps.synchronize()
        t1 = now()
        samples.append(t1 - t0)
    return samples

# ---------------- CPU DRAM Thrash Kernel ----------------
def cpu_mem_thrash(duration_s=5, size_mb=1024):
    arr = np.zeros((size_mb * 1024 * 1024) // 8, dtype=np.float64)
    t_end = now() + duration_s
    i = 0
    while now() < t_end:
        arr[(i % arr.size)::64] += 1.0
        i += 1
    return float(arr.sum())

# ---------------- GPU AXPY Kernel ----------------
def gpu_axpy_timed(n=64*1024*1024, dtype=torch.float32):
    device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
    a = torch.tensor(2.0, dtype=dtype, device=device)
    x = torch.randn(n, dtype=dtype, device=device)
    y = torch.randn(n, dtype=dtype, device=device)
    def fn():
        y.add_(x, alpha=float(a))
    return summarize(bench_sync(fn, warmup=2, iters=8, synchronize_gpu=True))

# ---------------- Main Sweep ----------------
if __name__ == "__main__":
    sizes_gb = [1, 2, 4, 8]         # CPU thrash sizes in GB
    num_procs = [1, 2, 4, 8]       # Number of CPU thrash processes
    duration_s = 6
    n_axpy = 64*1024*1024          # 64M elements (256 MB for float32)

    print(f"Running GPU contention sweep using Python interpreter: {sys.executable}")

    baseline = gpu_axpy_timed(n=n_axpy)
    print("Baseline GPU AXPY:", baseline)

    results = []
    for size in sizes_gb:
        for pcount in num_procs:
            print(f"Running contention test: {size} GB × {pcount} proc(s)")
            procs = [mp.Process(target=cpu_mem_thrash, kwargs={"duration_s": duration_s, "size_mb": size*1024})
                     for _ in range(pcount)]
            for p in procs: p.start()
            cont = gpu_axpy_timed(n=n_axpy)
            for p in procs: p.join()
            results.append({"size_gb": size, "procs": pcount, "mean_s": cont["mean_s"]})

    df = pd.DataFrame(results)
    print(df)

    pivot = df.pivot(index="size_gb", columns="procs", values="mean_s")
    plt.figure(figsize=(8,6))
    plt.imshow(pivot, aspect="auto", origin="lower", cmap="inferno")
    plt.colorbar(label="GPU AXPY Mean Time (s)")
    plt.xticks(range(len(pivot.columns)), pivot.columns)
    plt.yticks(range(len(pivot.index)), [f"{i} GB" for i in pivot.index])
    plt.xlabel("Number of CPU Thrash Processes")
    plt.ylabel("CPU Thrash Size")
    plt.title("GPU Latency under CPU DRAM Contention (M4 Pro)")
    plt.tight_layout()
    plt.savefig("contention_heatmap.png", dpi=150)
    print("Plot saved as contention_heatmap.png")
