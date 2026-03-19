# Contributing to TASD Core Framework

Thanks for your interest in contributing! TASD Core is the capstone framework for the Toroidal-Attractor Signal Dynamics suite.

## Ways to Contribute

- **Bug reports** — open an issue describing the problem, your Python version, and steps to reproduce.
- **Feature requests** — open an issue with a clear description of the proposed feature and its relevance to TASD signal dynamics.
- **Code contributions** — fork the repo, make your changes, and submit a pull request.
- **Physics / signal processing feedback** — if you spot modeling issues or have suggestions for improving the toroidal attractor dynamics, open an issue or discussion.

## Guidelines

1. **Python code** — keep dependencies minimal. NumPy and SciPy are acceptable; heavy frameworks should be justified.
2. **Reproducibility** — all examples and benchmarks should be deterministic or clearly document their random seed.
3. **Documentation** — update `TASD_Core_Overview.md` if your changes affect the framework's architecture or API.
4. **Test before submitting** — verify your changes run cleanly with `python tasd_quick_example.py` at minimum.
5. **Respect the framework** — TASD Core implements toroidal-attractor signal dynamics for plasma control and signal processing. Keep that framing in any documentation.

## Pull Request Process

1. Fork and create a feature branch (`git checkout -b feature/my-feature`).
2. Make your changes.
3. Test thoroughly.
4. Submit a PR with a clear description of what changed and why.

## License

By contributing, you agree that your contributions will be licensed under the existing license terms.

## Contact

For questions, reach out to **Nicolas B. Quiroz, MD** via [GitHub](https://github.com/BEPframework).
