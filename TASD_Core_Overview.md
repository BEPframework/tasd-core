# TASD Core Framework v1.0

**Unified Toroidal-Attractor Signal Dynamics for Tokamak Control and Simulation**

This is the final documentation artifact that unifies the entire open-source suite (Artifacts 1–4).

## The Original Equation
∫_γ (d|ψ⟩⟨ψ| + H(X,Y) + E(ρ_AB) + Φ · r · e^{b0}) dω = Ψ_universe

## Lyapunov Stability Sketch
V(e) = (1/2)‖e‖²  
V̇(e) ≤ -(γ/2) V  
→ Sketch only: assumes the attraction term dominates the disturbances. Not a complete proof.

## Exploratory Test
Psi v2 was run on the plasma-current trace of one EAST discharge (#41195) with synthetic noise, wall drift and actuator delay added. The earlier reported figure (output std 0.274) is withdrawn until a reproducible benchmark with tracking-error metrics is published; see the psi-universe-attractor README.

## The Full Suite
- Artifact 1: Psi Universe Attractor Library v2.0
- Artifact 2: Toroidal Dynamics Toolkit
- Artifact 3: TASD Unified Framework
- Artifact 4: Q216D Tokamak Simulation

This is an exploratory open-source framework for attractor-based tokamak signal processing; it has not been validated for control.

Citation: Quiroz, N. B. (2026). TASD Core Framework v1.0. Zenodo. https://doi.org/10.5281/zenodo.18928047
