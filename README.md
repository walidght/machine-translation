# English-to-French Translation Model Using Seq2Seq Architecture

This project focuses on developing a character-level English-to-French translation model using a Seq2Seq architecture. Leveraging the core components of deep learning for language processing, The code showcases the steps from data preprocessing to using LSTMs to build a sequence-to-sequence (Seq2Seq) model with keras.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture and Approach](#architecture-and-approach)
3. [Technical Skills](#technical-skills)
4. [File Descriptions](#file-descriptions)
5. [Setup and Usage](#setup-and-usage)
6. [Future Improvements](#future-improvements)

## Project Overview

The main goal of this project is to develop a robust translation model that accurately translates English sentences to French. Given the constraints of CPU resources, only a subset of the original 200k-sentence dataset was used, allowing the model to learn essential translation mappings while mitigating overfitting. The pipeline is split into three stages: data preprocessing, model training, and testing, each documented in separate notebooks.

## Architecture and Approach

This translation model is built on a Seq2Seq architecture, a standard choice for machine translation tasks. Key components of the architecture include:

- **Encoder-Decoder Framework**: The encoder processes the English input and encodes it into a fixed-size context vector. The decoder then uses this context vector to generate the corresponding French translation, character by character.
- **LSTM Layers**: Long Short-Term Memory (LSTM) units form the core of both the encoder and decoder. The LSTMs capture temporal dependencies in the sequence data, essential for language modeling tasks.
- **Character-Level Embedding**: Each character in the input and output sequences is represented with an embedding, allowing the model to learn translation at the character level. This approach simplifies vocabulary handling, though it necessitates careful handling of sequence length and batch sizes.

## Technical Tasks

This project emphasizes several technical skills and concepts fundamental to neural machine translation and deep learning:

- **Data Preprocessing with Pandas**: The dataset required significant cleaning to normalise the sentences and remove duplicate sentences and ensure a balanced training set. This preprocessing was managed with Pandas, allowing for efficient data manipulation and sampling.
- **LSTM and Seq2Seq Modeling with Keras**: Building the model structure required understanding the LSTM mechanics and the Seq2Seq architecture, particularly with respect to state propagation between the encoder and decoder during inference.
- **Model Evaluation**: Loss and Accuracy of the generated translations was evaluated against a held-out test set, and metrics were monitored to identify areas of improvement.
  
## File Descriptions

- **1-data-cleaning.ipynb**: This notebook covers data preprocessing steps, including the removal of duplicates, sentence tokenisation, and sampling to manage resource constraints.
- **2-training-model.ipynb**: In this notebook, the Seq2Seq model is trained. The model architecture includes an auto encoder with LSTMs, optimized for the translation task.
- **3-testing-model.ipynb**: This notebook demonstrates the inference process, where the trained model translates unseen English sentences to French. Various translations are evaluated to gauge model performance.

## Setup and Usage

### Prerequisites

- Python 3.x
- Keras
- Numpy
- Pandas
- Matplotlib

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/walidght/translation-model.git
   ```

2. Navigate into the project directory and install dependencies:
   ```bash
   cd translation-model
   pip install -r requirements.txt
   ```

### Running the Notebooks
Each notebook contains step-by-step instructions for running the code. It is recommended to follow the sequence from ```1-data-cleaning.ipynb``` through ```3-testing-model.ipynb```.

## Future Improvements
Given additional resources, potential improvements include:
- Increased Dataset Size: Expanding the training set to include more sentence pairs would provide the model with richer language mappings.
- Model Tuning: Experiment with deeper layers, attention mechanisms, or other architecture variations to improve model performance.
- Deployment: Package the model into an API for real-time translation.