# TASD Core v1.0

**Official Python implementation of the Ψ_universe attractor and the Toroidal-Attractor Signal Dynamics (TASD) framework.**

This library provides the clean, modular core mathematics behind ultra-precise state stabilization using the original Ψ_universe equation.

### ✨ Key Features
- Full Ψ_universe attractor equation with dissipative oscillatory dynamics
- Configurable parameters (gamma decay, Hurst exponent, turbulence, dimension)
- Built-in PCA reduction to lower-dimensional latent space
- Parameter optimizer and stability tools
- Signal evolution and attractor filtering functions
- Easy integration with NumPy, SciPy and scikit-learn
- Numerically stable attractor behavior for research and simulations

### 🚀 Quick Start
```python
from tasd import TASD
import numpy as np

# Initialize the attractor
tasd = TASD(dim=216, gamma=0.05, hurst=0.8)

# Example input (e.g. plasma features)
X = np.random.uniform(2.0, 3.0, size=(500, 12))

# Evolve through the attractor
output = tasd.evolve(X, t=5.0)

print("Output shape:", output.shape)
print("Stabilized range:", output.min(), "—", output.max())
```

## Patent Pending

This library implements the **TASD framework** and **Ψ_universe attractor** from **US Provisional Patent Application filed January 12, 2026 by Nicolas B. Quiroz, MD.**

---

## License

**Apache License 2.0** — see the [LICENSE](LICENSE) file for details.

---

## Citation

Quiroz, N. B. (2026). *TASD Core v1.0* [Software]. Zenodo.  
https://doi.org/10.5281/zenodo.18928047
