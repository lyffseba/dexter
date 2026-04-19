# Dexter 🚀

This repository contains everything needed to spin up, run, and fine-tune Large Language Models (like `google/gemma-4-31B`) on cheap, high-performance cloud GPUs.

## 🌟 The Best Platform: RunPod

For cost-to-performance, **RunPod.io** is currently the best platform. You can rent an RTX 3090 (24GB) or RTX 4090 (24GB) for ~$0.20 to $0.40 per hour, which is perfect for running the 31B model in 4-bit, or an A6000 (48GB) to run it in 8-bit.

---

## 🛠️ Getting Started on RunPod

### 1. Account Setup
1. Go to [RunPod.io](https://www.runpod.io) and create an account.
2. Add a few dollars in billing credits (e.g., $10).
3. Go to **Deploy -> Secure Cloud**.

### 2. Spinning up the Instance
1. Select a GPU: 
   - **1x RTX 3090 / 4090 (24GB VRAM)** (Good for 4-bit)
   - **1x A6000 / RTX 6000 Ada (48GB VRAM)** (Best for 8-bit / Fine-tuning)
2. Select Template: `RunPod PyTorch 2.x` (or type "PyTorch" in the search bar).
3. Ensure you allocate at least **60 GB of Volume Disk** to hold the model weights.
4. Click **Deploy**.

### 3. Accessing the Workspace
Once deployed, click **Connect**. You will have access to a Jupyter Lab environment.
Open a Terminal inside Jupyter Lab and clone this repository (or just copy the setup scripts).

---

## 🚀 Running Gemma-4-31B (Inference)

Inside your RunPod terminal, run the setup script:

```bash
bash scripts/01_setup_inference.sh
```

Then start the OpenAI-compatible server using vLLM:

```bash
bash scripts/02_start_server.sh
```

Now you can interact with the model via Python or using a UI!

---

## 🔬 Tinkering & Fine-Tuning Labs

Check the `labs/` directory for Jupyter Notebooks designed to let you play with the model.
- `labs/01_inference_test.ipynb`: Test prompting and generating text.
- `labs/02_qlora_finetuning.ipynb`: Learn how to fine-tune Gemma-4-31B on your own custom data using LoRA.
