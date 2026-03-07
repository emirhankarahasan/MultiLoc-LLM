# 🎮 MultiLoc-LLM: Specialized LLM for Game Localization

This repository contains an end-to-end pipeline to fine-tune **Meta's Llama-3-8B** for professional game localization tasks. The model is specifically optimized to handle game-specific context and terminology between **English, Turkish, and German**.

## 🌟 Project Highlights
- **Base Model:** Llama-3-8B-Instruct (via Unsloth)
- **Methodology:** Parameter-efficient fine-tuning using **LoRA** (Low-Rank Adaptation).
- **Data Source:** Curated and cleaned localization files from *The Battle for Wesnoth*.
- **Quantization:** Exported to **4-bit GGUF** for seamless local inference.

## 📁 Repository Structure
- `*.ipynb`: The complete Google Colab notebook containing setup, training, and inference steps.
- `*.jsonl`: The cleaned multilingual dataset used for fine-tuning.
- **Hugging Face Model:** [MODEL_LİNKİNİ_BURAYA_YAPIŞTIR]

## 🛠 Skills Demonstrated
- **Data Engineering:** Extracting and formatting raw game strings into LLM-ready JSONL.
- **NLP & Fine-Tuning:** Implementing SFT (Supervised Fine-Tuning) using Hugging Face's TRL library.
- **Model Optimization:** Converting models to GGUF for consumer-grade hardware compatibility.
- **Localization Engineering:** Bridging the gap between traditional translation and modern AI workflows.

## 🚀 How to Run
1. Upload the `.ipynb` file to Google Colab.
2. Ensure you have a Hugging Face "Write" token.
3. Run all cells to replicate the training process or use the provided GGUF model in **LM Studio**.
