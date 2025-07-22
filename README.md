# Financial Complaint Classification using Topic Modeling

This project uses **BERTopic**, a powerful topic modeling library, to automatically classify financial complaints into relevant categories. The trained model is served through a user-friendly web interface built with **Streamlit**.

## 🚀 Overview

The primary goal of this project is to take a user's financial complaint as input, process it, and then predict which department or category the complaint belongs to. This is achieved by leveraging state-of-the-art NLP models for creating document embeddings and clustering them into coherent topics.

The final application allows a user to enter their complaint into a text box, and upon submission, it displays the predicted topic, such as "Debt, Loan & Mortgage" or "Credit Report, Company & Identity Theft".

## 🛠️ How It Works

The project follows a standard machine learning pipeline:

### 1. Data Preprocessing (`pre_process_data.py`)

Before training the topic model, the text data (financial complaints) undergoes a series of cleaning steps:
- **Text Cleaning**: Unnecessary characters, such as punctuation and extra spaces, are removed.
- **Stopword Removal**: Common English words that do not add significant meaning (e.g., "the", "a", "is") are filtered out.
- **Lemmatization**: Words are reduced to their base or root form (e.g., "running" becomes "run") to standardize the vocabulary.

### 2. Topic Modeling with BERTopic (`BERTopic (1).ipynb`)

The core of this project is the BERTopic model, which is configured with several components to identify topics from the complaint data:

- **Embeddings**: The `all-MiniLM-L6-v2` model from `sentence-transformers` is used to convert the text of each complaint into a dense vector representation (embedding). These embeddings capture the semantic meaning of the text.

- **Dimensionality Reduction**: **UMAP** (Uniform Manifold Approximation and Projection) is used to reduce the dimensionality of the embeddings. This step is crucial for making the clustering process more effective and efficient.

- **Clustering**: **HDBSCAN** (Hierarchical Density-Based Spatial Clustering of Applications with Noise) is used to group similar documents together based on their reduced embeddings. Each resulting cluster is considered a "topic."

- **Topic Representation**:
    - `CountVectorizer` is used to tokenize the documents.
    - `ClassTfidfTransformer` is then applied to find the most important words for each topic. It modifies the TF-IDF algorithm to work on a class-based (or topic-based) level, highlighting what makes each topic unique.
    - `KeyBERTInspired` is used as a representation model to fine-tune and improve the quality and coherence of the topic representations.

The trained BERTopic model is then saved to a file (`./static/final_model`) so it can be loaded for inference without needing to be retrained.

### 3. Prediction and Deployment (`index.py` and `pre_process_data.py`)

- The **Streamlit** application provides the front-end for the user.
- When a user submits a complaint, the `main_fun` function in `pre_process_data.py` is called.
- This function applies the same preprocessing steps to the user's input text.
- The pre-trained BERTopic model is loaded, and its `.transform()` method is used to predict the topic for the new complaint.
- The application then maps the predicted topic ID to a human-readable name (e.g., "Account & Fraud, Scam") and displays it to the user.

## 📂 File Descriptions

- **`index.py`**: The main Streamlit application script. It handles the user interface, form submission, and calls the prediction function.
- **`pre_process_data.py`**: Contains all the functions for text cleaning, preprocessing, and the main prediction logic that loads the saved BERTopic model.
- **`BERTopic (1).ipynb`**: A Jupyter Notebook that details the entire process of loading the data, preprocessing it, training the BERTopic model, and saving it. This serves as the development and experimentation environment.
- **`static/final_model`**: The saved, pre-trained BERTopic model file that is loaded by the application for making predictions.
- **`styles.css`**: Contains the CSS for styling the Streamlit application.

## ⚙️ How to Run the Application

1.  **Install the required libraries**:
    ```bash
    pip install streamlit pandas numpy torch bertopic sentence-transformers scikit-learn nltk
    ```
2.  **Download NLTK data**:
    Run the following in a Python interpreter:
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    nltk.download('wordnet')
    ```
3.  **Ensure the model file is present**:
    Make sure the saved BERTopic model is located at `./static/final_model`.
4.  **Run the Streamlit app**:
    Open your terminal, navigate to the project's root directory, and run:
    ```bash
    streamlit run index.py
    ```
5.  Open your web browser and go to the local URL provided by Streamlit.

