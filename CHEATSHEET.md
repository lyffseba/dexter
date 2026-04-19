# 🚀 Dexter OS: Director's Cheat Sheet

Welcome to the autonomous AI research swarm. This is your quick-reference guide to the ecosystem we've built, the tools at your disposal, and your exact first steps.

---

## 🎮 First Steps: The Interactive OS
You don't need to memorize long commands. Everything is managed through the custom Python interface.

1. **Open a terminal** in the `dexter` repository folder:
   ```bash
   cd ~/lyff/dexter
   ```
2. **Launch the OS:**
   ```bash
   python3 dexter_cli.py
   ```
3. **The Menu:** You will see your current RunPod balance ($10) and 5 options:
   * `[1] Lab 00`: Launches the interactive Jupyter tutorial. Start here!
   * `[2] Lab 03`: Compiles the raw `train.mojo` file locally using the Modular MAX framework.
   * `[3] RUNPOD`: The big button. Deploys an RTX 3090 GPU in the cloud.
   * `[4] MODULAR`: Prints the instructions for starting a production API.
   * `[5] EXIT`: Closes the OS.

---

## 🗂️ Project Structure
What is actually inside this repository?

* **`dexter_cli.py`**: The game/control center.
* **`labs/`**: All the isolated AI experiments.
  * `docs/`: Dedicated `README.md` files for every single lab.
  * `00_getting_started.ipynb`: The local introduction to data and tokenizers.
  * `01_inference_test.ipynb`: How to prompt an AI API.
  * `02_qlora_finetuning.ipynb`: How to train Gemma-4 on custom data.
  * `autoresearch/`: The autonomous PyTorch agent that invents new AI architectures.
    * `mojo/`: The ongoing port of the `autoresearch` AI into the **Mojo 🔥** language.
* **`scripts/`**: The deployment bash files to install MAX and serve `Gemma-4-31B`.

---

## 🛠️ The Tech Stack (How it works under the hood)

*   **`uv`**: The blazing-fast Python package manager. It keeps all Python dependencies strictly locked inside `.venv` folders so your laptop never breaks.
*   **`pixi`**: The cross-platform package manager. We use this exclusively in `labs/autoresearch/mojo/` to download and isolate the **Mojo Compiler** and **Modular MAX Engine**.
*   **Modular MAX**: The inference engine we use instead of `vLLM` because it is 15% faster on B200 and MI355 GPUs.
*   **RunPod**: The cloud provider we use for training (where your $10 lives).

---

## 🔄 Syncing the Swarm
If you ever make changes locally, the entire repo is synchronized to two places:
1. **GitHub:** The `main` and `autoresearch/apr19` branches.
2. **Hugging Face Model Hub:** The repository `lyffseba/dexter`.

*Note: Huge virtual environments (`.venv`, `.pixi`) are strictly `.gitignore`'d and excluded from Hugging Face uploads to keep the repo lightning fast.*
