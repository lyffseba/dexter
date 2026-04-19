# Contributing to Dexter

First off, thank you for considering contributing to Dexter! It's people like you that make Dexter such a great ecosystem for tinkering and fine-tuning Large Language Models.

## 🤝 How to Contribute

### 1. Code of Conduct
By participating in this project, you are expected to uphold our standard community guidelines. Be respectful, inclusive, and collaborative.

### 2. Issues & Bug Reports
- Check if the issue already exists.
- If it doesn't, create a new issue.
- Clearly describe the bug: what happened, what you expected to happen, and how to reproduce it.

### 3. Submitting Pull Requests
1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs or added new Labs, update the documentation in `labs/docs/`.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## 🔬 Adding New Labs
If you want to contribute a new interactive notebook or AI research loop:
1. Place it inside the `labs/` directory.
2. Ensure it is **100% self-contained** (use `uv` or `pixi` for dependencies, avoid polluting global environments).
3. Create a dedicated `README.md` for it inside `labs/docs/<lab_name>/`.
4. Update the root `README.md` to link to your new lab.

## 🚀 Environment Standards
We strictly use:
- **[uv](https://docs.astral.sh/uv/)** for lightning-fast Python package management.
- **[Pixi](https://pixi.sh/)** for managing native dependencies and the **Mojo 🔥** compiler.
- **MAX** for inference deployment.

Please do not introduce `requirements.txt` or standard `pip` workflows into new labs. Stick to the modern ecosystem!

---
*Happy Tinkering!*