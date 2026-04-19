# Lab 01: Inference Test & Prompting

## Overview
This lab is designed to verify the cloud deployment and test basic prompting and text generation capabilities of the deployed model (e.g., `Gemma-4-31B`).

## Setup
Ensure you have spun up the Modular Cloud MAX Engine or a RunPod inference endpoint (using `scripts/01_setup_inference.sh` and `02_start_server.sh`).

## Usage
Open `01_inference_test.ipynb` in a Jupyter environment. The notebook contains examples of:
1. Connecting to the OpenAI-compatible API endpoint.
2. Constructing basic prompts.
3. Testing generation speed and context limits.

## Goals
- Verify API connectivity.
- Understand basic prompting structures.
- Measure inference latency (tokens per second).