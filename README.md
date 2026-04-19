<div align="center">

# 🚀 Dexter

**The Ultimate Ecosystem to Spin Up, Run, and Fine-Tune Large Language Models**

[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model_Repo-ffcc66.svg?style=for-the-badge)](https://huggingface.co/lyffseba/dexter)
[![Modular MAX](https://img.shields.io/badge/Powered_by-Modular_MAX-007FFF.svg?style=for-the-badge)](https://docs.modular.com/max/)
[![Mojo](https://img.shields.io/badge/Language-Mojo_%F0%9F%94%A5-FF4500.svg?style=for-the-badge)](https://docs.modular.com/mojo/)
[![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

</div>

---

> [!IMPORTANT]
> **Dexter** provides a straight line from your first API call to autonomous AI research loops and production endpoints. Designed for `Gemma-4-31B` and optimized for cheap, high-performance cloud GPUs.

## 🎮 The Dexter OS (Start Here!)
The easiest way to interact with the entire ecosystem, run labs, and manage your cloud swarm is through the interactive Dexter OS CLI.

```bash
# Clone the repository
git clone https://github.com/lyffseba/dexter.git
cd dexter

# Boot up the Dexter OS
python3 dexter_cli.py
```
*The OS will guide you through running the local Mojo labs and deploying the cloud inference endpoints automatically.*

## 🗂️ Ecosystem Structure

```text
dexter/
├── scripts/                 # Deployment scripts for Inference (Modular MAX)
└── labs/                    # Interactive Tinkering & Fine-Tuning Labs
    ├── docs/                      # 📖 Dedicated documentation per lab
    ├── 00_getting_started.ipynb   # 🟢 START HERE: Data, Tokenizers & Mojo setup
    ├── 01_inference_test.ipynb    # 💬 API Prompting & Generation
    ├── 02_qlora_finetuning.ipynb  # 🧠 QLoRA fine-tuning 31B models
    └── autoresearch/              # 🤖 Autonomous AI Agent Research Loop (PyTorch -> Mojo port)
```

## 🌟 The Best Platform: Modular Cloud

For cost-to-performance, **[Modular Cloud](https://console.modular.com)** is currently the best platform. They have the fastest inference speeds for `Gemma-4` using **MAX**, their GenAI native modeling & serving framework, completely outperforming vLLM on both NVIDIA and AMD platforms.

> [!TIP]
> While Modular Cloud is ideal for inference and deployment, **RunPod** (RTX 3090/4090) remains the best value for bare-metal SSH access required for the autonomous PyTorch training labs.

---

## 🛠️ Getting Started on Modular Cloud

### 1. Account Setup
1. Go to the [Modular Console](https://console.modular.com) and sign up.
2. Modular Cloud gives you a straight line from the first API call to a production endpoint.

### 2. Running Gemma-4-31B (Inference)

Inside your cloud environment, install the Modular CLI and MAX framework:

```bash
bash scripts/01_setup_inference.sh
```

Then start the MAX engine server:

```bash
bash scripts/02_start_server.sh
```

Now you can interact with the model via Python or using any OpenAI-compatible UI!

---

## 🔬 Tinkering & Fine-Tuning Labs

Check the `labs/` directory for Jupyter Notebooks designed to let you play with the model locally and in the cloud.

- **[START HERE]** [`labs/00_getting_started.ipynb`](labs/00_getting_started.ipynb): An interactive, local introduction to AI data, tokenizers, and compiling Mojo. Start here to learn the fundamentals!
- [`labs/01_inference_test.ipynb`](labs/01_inference_test.ipynb): Test prompting and generating text against your MAX endpoint.
- [`labs/02_qlora_finetuning.ipynb`](labs/02_qlora_finetuning.ipynb): Learn how to fine-tune `Gemma-4-31B` on your own custom data using LoRA.
- [`labs/autoresearch/`](labs/autoresearch/): An autonomous AI agent loop that tweaks LLM architectures. Includes the ongoing project to port the framework from PyTorch to **Mojo 🔥 & MAX**.

---

<div align="center">
  <i>Built with ❤️ by lyffseba and the autonomous swarm</i>
</div>