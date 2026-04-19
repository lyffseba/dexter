# Dexter 🚀

This repository contains everything needed to spin up, run, and fine-tune Large Language Models (like `google/gemma-4-31B`) on cheap, high-performance cloud GPUs.

## 🌟 The Best Platform: Modular Cloud

For cost-to-performance, **Modular Cloud** is currently the best platform. They have the fastest inference speeds for Gemma 4 using MAX, their GenAI native modeling & serving framework, completely outperforming vLLM on both NVIDIA and AMD platforms.

---

## 🛠️ Getting Started on Modular Cloud

### 1. Account Setup
1. Go to [Modular Console](https://console.modular.com) and sign up.
2. Modular Cloud gives you a straight line from first API call to production endpoint.

---

## 🚀 Running Gemma-4-31B (Inference)

Inside your environment, install the Modular CLI and MAX:

```bash
bash scripts/01_setup_inference.sh
```

Then start the MAX engine server:

```bash
bash scripts/02_start_server.sh
```

Now you can interact with the model via Python or using a UI!

---

## 🔬 Tinkering & Fine-Tuning Labs

Check the `labs/` directory for Jupyter Notebooks designed to let you play with the model.
- `labs/01_inference_test.ipynb`: Test prompting and generating text.
- `labs/02_qlora_finetuning.ipynb`: Learn how to fine-tune Gemma-4-31B on your own custom data using LoRA.
- `labs/autoresearch/`: An autonomous AI agent loop that tweaks LLM architectures. Includes the ongoing project to port the framework to **Mojo & MAX**.
