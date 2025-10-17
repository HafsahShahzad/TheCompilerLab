import time
import numpy as np
import matplotlib.pyplot as plt

def cpu_heavy_task(n: int = 3_000_000):
    print("[CPU] Starting heavy computation...")
    x = np.random.rand(n)
    y = np.random.rand(n)
    result = np.dot(x, y)
    print(f"[CPU] Dot product result: {result:.4f}")

def gpu_heavy_task():
    print("[GPU] Generating large figure...")
    fig, ax = plt.subplots(figsize=(12, 12), dpi=300)
    x = np.linspace(-3, 3, 2000)
    y = np.linspace(-3, 3, 2000)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X**2 + Y**2) / (X**2 + Y**2 + 1e-6)
    ax.imshow(Z, extent=(-3, 3, -3, 3), origin='lower', cmap='viridis')
    ax.set_title("GPU Heatmap")
    plt.savefig("gpu_render_output.png", bbox_inches='tight')
    plt.close(fig)
    print("[GPU] Finished rendering and saved image.")

def main():
    start = time.time()
    cpu_heavy_task()
    gpu_heavy_task()
    end = time.time()
    print(f"[INFO] Total runtime: {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
