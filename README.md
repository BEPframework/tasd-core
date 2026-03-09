# TASD Core v1.0

**Official Python implementation of the Ψ_universe attractor and the Toroidal-Attractor Signal Dynamics (TASD) framework.**

This library delivers the clean, modular core mathematics behind ultra-precise state stabilization using the original Ψ_universe equation.

### What is TASD?
TASD is a compact attractor-based filter that improves state separation in high-dimensional, nonstationary signals. It projects input features into a dissipative oscillatory space, applies controlled turbulence, reduces dimensionality via PCA, and produces a numerically stable output suitable for plasma control, physiological signal processing, and other precision-critical applications.

### ✨ Key Features
- Full Ψ_universe attractor equation with dissipative oscillatory dynamics
- Configurable parameters (gamma decay, Hurst exponent, turbulence, dimension)
- Built-in PCA reduction to lower-dimensional latent space
- Parameter optimizer and stability tools
- Signal evolution and attractor filtering functions
- Easy integration with NumPy, SciPy and scikit-learn
- Numerically stable attractor behavior for research and simulations

### 🚀 Quick Start
Copy `tasd.py` into your project (or add it to your Python path) and start using it immediately.

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
