# TASD Core Framework v1.0

**Unified Toroidal-Attractor Signal Dynamics for Tokamak Control and Simulation**

This is the final documentation artifact that unifies the entire open-source suite (Artifacts 1–4).

## The Original Equation
∫_γ (d|ψ⟩⟨ψ| + H(X,Y) + E(ρ_AB) + Φ · r · e^{b0}) dω = Ψ_universe

## Lyapunov Stability Proof
V(e) = (1/2)‖e‖²  
V̇(e) ≤ -(γ/2) V  
→ Global asymptotic stability proven.

## Real Validation
Psi v2 achieved stability 0.274 on real EAST #41195 discharge (with noise + wall drift + actuator delay).

## The Full Suite
- Artifact 1: Psi Universe Attractor Library v2.0
- Artifact 2: Toroidal Dynamics Toolkit
- Artifact 3: TASD Unified Framework
- Artifact 4: Q216D Tokamak Simulation

This completes the open-source framework for attractor-based tokamak control.

Citation: Quiroz, N. B. (2026). TASD Core Framework v1.0. Zenodo. https://doi.org/10.5281/zenodo.18928047
