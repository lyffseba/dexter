# Autoresearch: Mojo & MAX Port

This directory contains the ongoing effort to port the PyTorch-based `autoresearch` training loop into **Mojo** and the **Modular MAX** framework.

## Goals

1. **Performance**: Eliminate Python GIL and Garbage Collection stalls present in the original `train.py`.
2. **Hardware Intimacy**: Use Mojo's `SIMD` and memory primitives to write custom attention mechanisms without relying on external CUDA kernels like FlashAttention.
3. **Serving**: Integrate the trained weights seamlessly into the MAX Engine for inference.

## Current Status
- [x] Initialized project structure.
- [ ] Porting `CausalSelfAttention` and `MLP` blocks to Mojo.
- [ ] Porting the Muon Optimizer to Mojo.
- [ ] Integrating MAX Graph compilation.

## How to run (Coming Soon)
```bash
magic run mojo mojo/train.mojo
```