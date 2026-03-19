[README.md](https://github.com/user-attachments/files/26102933/README.md)
# TASD Core Framework v1.0

**Toroidal-Attractor Signal Dynamics — Capstone Framework**

The capstone documentation and reference implementation for the complete open-source TASD suite, covering toroidal attractor dynamics for tokamak plasma control and frequency-domain signal processing.

---

### Overview

TASD Core unifies the theoretical and computational foundations of the Toroidal-Attractor Signal Dynamics framework. It serves as the entry point for understanding how the Ψ_universe attractor, toroidal modulation, and signal dynamics fit together as a coherent system.

See [`TASD_Core_Overview.md`](TASD_Core_Overview.md) for the full architectural details.

### Quick Start

```bash
python tasd_quick_example.py
```

No external dependencies beyond Python standard library and NumPy.

### Related Repositories

- [psi-universe-attractor](https://github.com/BEPframework/psi-universe-attractor) — Ψ_universe attractor filter, validated on real EAST #41195 data
- [tasd-framework](https://github.com/BEPframework/tasd-framework) — TASD Unified Framework (open-source release)
- [toroidal-dynamics-toolkit](https://github.com/BEPframework/toroidal-dynamics-toolkit) — Modular toolkit for dynamic toroidal modulation in frequency-domain signal processing
- [q216d-tokamak-simulation](https://github.com/BEPframework/q216d-tokamak-simulation) — Interactive 3D plasma visualization with TASD-enhanced control

### Copyright

Copyright © 2026 Nicolas B. Quiroz, MD. All rights reserved for the original work.

### License

See the [LICENSE](LICENSE) file for details.

### Citation

If you use this framework, please cite:

> **Quiroz, N. B. (2026)**. *TASD Core Framework v1.0*. Zenodo. https://doi.org/10.5281/zenodo.18928047

### Keywords

tokamak · fusion energy · plasma physics · toroidal plasma · magnetic confinement · plasma attractor dynamics
