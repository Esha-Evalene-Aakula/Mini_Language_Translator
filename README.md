# Mini Language Translator 

## Objective
The goal of this project is to build a simple translator that converts English sentences into Hindi.  
It demonstrates the use of pretrained sequence-to-sequence models for natural language translation and shows how a small dataset can be used to generate accurate translations.

---

## Tech Stack
- **Python 3.10+**: Programming language for all scripts and notebooks.
- **Hugging Face Transformers**: Provides pretrained MarianMT model for sequence-to-sequence translation.
- **PyTorch**: Backend framework required by Hugging Face models for model inference.
- **Pandas**: Used to manage and process the dataset of sentence pairs.
- **SentencePiece**: Required tokenizer library for MarianMT models.
- **Google Colab / Jupyter Notebook**: Recommended for running and visualizing the notebook step-by-step.

---

## Implementation Details

1. **Dataset Creation**  
   - A small dataset of ~30 English-Hindi sentence pairs is created within the code (no external upload required).  
   - Example sentence pair:  
     ```
     English: Hello, how are you?
     Hindi: नमस्ते, आप कैसे हैं?
     ```

2. **Model Loading**  
   - Pretrained MarianMT model `Helsinki-NLP/opus-mt-en-hi` is loaded using Hugging Face Transformers.  
   - The corresponding tokenizer is also loaded.

3. **Translation Function**  
   - English sentences are tokenized and passed through the model.  
   - Output tokens are decoded to get Hindi translations.

4. **Output**  
   - Translated sentences are printed alongside the original English sentences.  
   - Sample translations:
     ```
     Hello, how are you? → हैलो, तुम कैसे हो?
     I enjoy studying. → मुझे अध्ययन करने में मज़ा आता है।
     Good morning! → सुप्रभात!
     ```

---
Sample Output:


<img width="515" height="267" alt="image" src="https://github.com/user-attachments/assets/82368514-2775-4518-9af8-0f09bca84d5b" />
