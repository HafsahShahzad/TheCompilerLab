
import numpy as np
import torch
import multiprocessing as mp
import time
import matplotlib.pyplot as plt

def now():
    return time.perf_counter()

def cpu_mem_thrash(duration_s=5, size_mb=1024):
    arr = np.zeros((size_mb*1024*1024)//8, dtype=np.float64)
    t_end = now() + duration_s
    i = 0
    while now() < t_end:
        arr[(i % arr.size)::64] += 1.0
        i += 1
    return float(arr.sum())

def gpu_axpy_timed(n=64*1024*1024, dtype=torch.float32):
    device = torch.device("mps") if torch.backends.mps.is_available() else torch.device("cpu")
    a = torch.tensor(2.0, dtype=dtype, device=device)
    x = torch.randn(n, dtype=dtype, device=device)
    y = torch.randn(n, dtype=dtype, device=device)

    def fn():
        y.add_(x, alpha=float(a))

    if torch.backends.mps.is_available():
        torch.mps.synchronize()
    start = time.perf_counter()
    for _ in range(8):
        fn()
    if torch.backends.mps.is_available():
        torch.mps.synchronize()
    end = time.perf_counter()
    return {"mean_s": (end - start) / 8}

if __name__ == "__main__":
    print("Running GPU AXPY benchmark with CPU memory contention...")

    baseline = gpu_axpy_timed()
    print("Baseline AXPY GPU stats:", baseline)

    # launch CPU thrash in separate process
    p = mp.Process(target=cpu_mem_thrash, kwargs={"duration_s":6, "size_mb":1024})
    p.start()

    contended = gpu_axpy_timed()
    p.join()
    print("Contended AXPY GPU stats:", contended)

    means = [baseline["mean_s"], contended["mean_s"]]
    labels = ["Baseline", "With CPU DRAM Thrash"]

    plt.figure(figsize=(6,4))
    plt.bar(labels, means)
    plt.ylabel("Mean iteration time (s)")
    plt.title("GPU latency under CPU memory contention")
    plt.tight_layout()
    plt.savefig("contention_benchmark.png")
    print("Plot saved as contention_benchmark.png")
