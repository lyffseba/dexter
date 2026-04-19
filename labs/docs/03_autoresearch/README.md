# Lab 03: Autoresearch & Mojo Port

## Overview
This lab runs an autonomous AI research loop (`autoresearch`). An AI agent autonomously tweaks a PyTorch neural network (`train.py`), tests it for exactly 5 minutes, and measures validation loss (`val_bpb`) to discover new mathematical architectures. 

Additionally, this lab contains the **Mojo Port** (`mojo/`), translating the core Python/PyTorch attention math into the hyper-fast Mojo 🔥 language using the Modular MAX framework.

## Setup
### PyTorch Agent (`train.py`)
Run the Python agent locally or on a RunPod RTX 3090:
```bash
uv sync
uv run prepare.py
uv run train.py
```

### Mojo Port (`mojo/train.mojo`)
Run the Mojo compilation locally using Pixi:
```bash
cd mojo/
pixi run mojo train.mojo
```

## Goals
1. Understand autonomous AI loop structures (`program.md`).
2. Learn PyTorch `FlashAttention-3` and Muon optimizations.
3. Master Mojo's memory safety (`struct`), `SIMD` operations, and zero-cost abstractions by porting the `CausalSelfAttention` block.