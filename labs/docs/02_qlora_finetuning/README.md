# Lab 02: QLoRA Fine-Tuning

## Overview
This lab demonstrates how to efficiently fine-tune a massive model (like `Gemma-4-31B`) on consumer-grade hardware (like a single RunPod RTX 3090 or A6000) using QLoRA.

## Setup
You need a machine with at least 24GB of VRAM (e.g., an RTX 3090/4090 or A6000) running PyTorch with CUDA support.

## Usage
Open `02_qlora_finetuning.ipynb`. The notebook guides you through:
1. Loading the 31B model in 4-bit precision (bitsandbytes).
2. Setting up Low-Rank Adaptation (LoRA) to drastically reduce trainable parameters.
3. Formatting a custom dataset for instruct-tuning.
4. Running the HuggingFace `SFTTrainer`.

## Goals
- Learn how 4-bit quantization saves VRAM.
- Understand LoRA adapters.
- Successfully fine-tune the model to answer in a specific tone or learn a new specialized skill.