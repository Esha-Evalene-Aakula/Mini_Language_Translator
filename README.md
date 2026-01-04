# Mini Language Translator (English to Hindi)

## Overview

The Mini Language Translator is a simple natural language translation project that converts English sentences into Hindi. It demonstrates the use of pretrained sequence-to-sequence models for machine translation and shows how a small, curated dataset can be used to generate accurate translations.This project is intended for learning and experimentation with modern NLP models rather than large-scale production use.

## Objective

- Translate English sentences into Hindi
- Demonstrate sequence-to-sequence translation using pretrained models
- Showcase the use of Hugging Face Transformers with a small dataset

## Tech Stack

Programming Language ->	Python 3.10+
Translation Model ->	Hugging Face Transformers (MarianMT)
Deep Learning Backend -> PyTorch
Tokenization -> SentencePiece
Data Handling -> Pandas
Development Environment	-> Google Colab / Jupyter Notebook

## Key Features

- English to Hindi translation
- Uses a pretrained MarianMT sequence-to-sequence model
- Lightweight dataset embedded directly in code
- Easy to understand and extend for learning purposes

## Implementation Details

### Dataset Creation
- A small dataset of approximately 30 English–Hindi sentence pairs is created directly within the code
- No external dataset upload is required
- Each data entry contains an English sentence and its corresponding Hindi translation

  Example:
  <img width="317" height="74" alt="image" src="https://github.com/user-attachments/assets/29b232ba-29e4-4617-bb26-41e4a867a742" />


### Model Loading
- Pretrained MarianMT model Helsinki-NLP/opus-mt-en-hi is loaded using Hugging Face Transformers
- The corresponding tokenizer is initialized using SentencePiece

### Translation Process
- English sentence is tokenized using the MarianMT tokenizer
- Tokenized input is passed to the pretrained model
- Output tokens are decoded to generate the Hindi translation

### Output

- Translated Hindi sentences are displayed alongside the original English input
- Output is printed directly in the notebook or script for easy comparison

## Project Structure

<img width="629" height="165" alt="image" src="https://github.com/user-attachments/assets/5081c1fb-bb03-4931-9d6c-453e0fe736d0" />

## Future Enhancements

- Support for additional language pairs
- Batch translation and file-based input
- Web interface using Streamlit or Flask
- Larger datasets for improved translation accuracy
- Translation quality evaluation using BLEU or METEOR scores

## Conclusion

The Mini Language Translator demonstrates how pretrained sequence-to-sequence models can be effectively used for English-to-Hindi translation with minimal setup. It provides a solid foundation for understanding neural machine translation and experimenting with multilingual NLP systems.
