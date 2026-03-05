# MultiLoc-LLM: Multilingual Game Localization Data Pipeline

## Overview
This project is an automated data engineering pipeline designed to prepare raw game localization files for Large Language Model (LLM) fine-tuning. It extracts parallel text data from structured game files (JSON) and formats it into conversational `JSONL` structures for instruction-tuning.

## Features
* **Automated Language Detection:** Dynamically scans directories to identify source (en-US) and target languages.
* **Format Conversion:** Transforms Key-Value pairs into System/User/Assistant prompt structures.
* **Quality Assurance:** Automatically filters out empty or untranslated strings to prevent model hallucination.
* **Scalable Architecture:** Easily expandable to the standard EFIGS languages and beyond.

## Note on Data & Copyright
To respect intellectual property and copyright laws, no proprietary game text files or generated datasets are hosted in this repository. 
The provided `data_pipeline.py` script is designed to be executed locally by users who own the corresponding game files.