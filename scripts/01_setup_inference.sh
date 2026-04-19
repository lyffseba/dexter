#!/bin/bash
set -e

echo "🚀 Setting up Inference Environment for Gemma-4-31B..."

# Update pip
pip install --upgrade pip

# Install huggingface hub for downloading
pip install "huggingface_hub[cli]"

# Install vLLM for ultra-fast serving and memory management
pip install vllm

# Login to HuggingFace (Requires HF_TOKEN environment variable)
if [ -z "$HF_TOKEN" ]; then
    echo "⚠️ Warning: HF_TOKEN is not set. You might need it if the model requires accepting a license."
    echo "Run: export HF_TOKEN='your_token_here'"
else
    huggingface-cli login --token $HF_TOKEN
fi

# Download the model (we download it directly on the cloud instance because uploading 60GB takes too long)
echo "Downloading google/gemma-4-31B..."
huggingface-cli download google/gemma-4-31B --local-dir ./gemma-4-31B

echo "✅ Setup Complete!"
