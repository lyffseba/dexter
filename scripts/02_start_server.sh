#!/bin/bash

echo "🚀 Starting vLLM Server with Gemma-4-31B in 4-bit mode..."

# We use vLLM with AWQ or GPTQ if pre-quantized, but for raw weights on a 24GB card we use bitsandbytes 4-bit via load-format
# If you are on an A6000 (48GB), you can remove the --quantization flag.

python -m vllm.entrypoints.openai.api_server \
    --model ./gemma-4-31B \
    --quantization bitsandbytes \
    --load-format bitsandbytes \
    --max-model-len 4096 \
    --port 8000

# Note: Once this is running, your model acts exactly like the OpenAI API!
