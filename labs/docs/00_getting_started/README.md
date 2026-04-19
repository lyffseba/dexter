# Lab 00: Getting Started (The Simplest Starting Point)

## Overview
Welcome! Before spinning up massive cloud GPUs or diving into complex AI loops, this is the absolute best place to start. This lab provides a completely local, interactive introduction to the foundational concepts of AI training and the Modular ecosystem.

## Setup
No cloud GPU is required. This lab runs entirely on your local CPU.

If you don't have Jupyter installed, you can launch it using `uv`:
```bash
uv tool run --from jupyterlab jupyter-lab
```

## Usage
Open `00_getting_started.ipynb` in the Jupyter interface. The notebook is an interactive journey that walks you through:
1. **The Data:** Inspecting the raw `TinyStories` dataset.
2. **The Tokenizer:** Seeing how English sentences are translated into numerical tokens using our custom BPE tokenizer.
3. **The Mojo Compiler:** Compiling and executing our first Mojo code locally using the `pixi` package manager.

## Goals
- Understand the raw ingredients of an AI model (Data + Tokens).
- Verify your local Python environment can read parquet data shards.
- Verify your local `pixi` environment can successfully compile Mojo (`.mojo`) files.
- Establish the baseline knowledge needed to start writing Neural Network architectures in Lab 03.