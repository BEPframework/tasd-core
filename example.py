"""
TASD Core v1.0 - Example & Benchmark
Demonstrates the Ψ_universe attractor on synthetic plasma-like data.
"""

import numpy as np
import time
from tasd import TASD

print("=" * 60)
print("TASD Core v1.0 - Example & Benchmark")
print("=" * 60)

# Initialize the attractor
tasd = TASD(dim=216, gamma=0.05, hurst=0.8)
print(f"✓ Attractor initialized (dim={tasd.dim}, gamma={tasd.gamma}, hurst={tasd.hurst})")

# Generate example input (plasma-like features)
X = np.random.uniform(2.0, 3.0, size=(1000, 12))
print(f"✓ Input data shape: {X.shape}")

# Evolve through the attractor
start = time.time()
output = tasd.evolve(X, t=5.0)
elapsed = time.time() - start

print(f"\n✓ Evolved in {elapsed:.4f} seconds")
print(f"  Output shape     : {output.shape}")
print(f"  Stabilized range : {output.min():.6f} — {output.max():.6f}")

# Optimize gamma for better stability
print("\nOptimizing gamma for tighter stability...")
start = time.time()
new_gamma = tasd.optimize_gamma(X, target_stability=0.001)
elapsed = time.time() - start
print(f"✓ Optimized gamma = {new_gamma:.4f} (took {elapsed:.2f}s)")

# Re-run with optimized gamma
output_opt = tasd.evolve(X, t=5.0)
print(f"  Final stabilized range : {output_opt.min():.6f} — {output_opt.max():.6f}")

print("\n✅ TASD attractor ready for research use!")
print("   (Patent Pending — US Provisional filed Jan 12, 2026)")
