"""Verifica dell'ambiente `cardio-ai` (imaging + AI).

Controlla che PyTorch veda la GPU Apple (MPS), misura un semplice prodotto
matriciale su CPU e GPU e verifica che TotalSegmentator sia importabile.

Uso:
    conda activate cardio-ai
    python scripts/check_env_ai.py
"""

import time

import nibabel
import SimpleITK as sitk
import torch
import totalsegmentator


def matmul_benchmark(device, n=4096, repeats=5):
    a = torch.randn(n, n, device=device)
    b = torch.randn(n, n, device=device)
    (a @ b).sum().item()  # riscaldamento
    t0 = time.perf_counter()
    for _ in range(repeats):
        c = a @ b
    c.sum().item()  # forza la sincronizzazione con la GPU
    return (time.perf_counter() - t0) / repeats


if __name__ == "__main__":
    from importlib.metadata import version

    print(f"torch {torch.__version__} | TotalSegmentator {version('TotalSegmentator')} "
          f"| SimpleITK {sitk.Version_VersionString()} | nibabel {nibabel.__version__}")
    mps = torch.backends.mps.is_available()
    print(f"GPU Apple (MPS) disponibile: {mps}")

    t_cpu = matmul_benchmark("cpu")
    print(f"[CPU] matmul 4096x4096: {t_cpu * 1000:.0f} ms")
    if mps:
        t_mps = matmul_benchmark("mps")
        print(f"[MPS] matmul 4096x4096: {t_mps * 1000:.0f} ms  (speed-up x{t_cpu / t_mps:.1f})")

    print("ESITO:", "OK" if mps and totalsegmentator else "PROBLEMA")
