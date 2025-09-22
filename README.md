# Log-Classification-System

This repository contains a system for classifying log messages using a combination of clustering, regex-based rules, and machine learning models. The project is designed to process and categorize log data from various sources into meaningful labels such as "HTTP Status," "Security Alert," and "Critical Error", "Workflow Error" etc.

---

## Classification Approaches

1. **Regular Expression (Regex)**:
   - Targets straightforward and predictable log message patterns.
   - Ideal for rule-based classification of common events like "User Action" or "System Notification" using predefined patterns.

2. **Sentence Transformer + ML Classification Models**:
   - Handles intricate patterns with adequate training data.
   - Leverages embeddings from Sentence Transformers to capture semantic meaning, with several classification algorithms for robust decision-making.

3. **LLM (Large Language Models)**:
   - Addresses complex patterns when labeled data is scarce.
   - Serves as a flexible fallback or supplementary method for rare or ambiguous log classifications.

- **DeepSeek R1 LLM**: Provides an additional layer of validation for complex or rare log patterns where labeled data is limited.
- **ML Models**: Ensures consistency by comparing predictions from Random Forest, Naive Bayes, and Logistic Regression, which demonstrated high accuracy.

This multi-model verification strengthens the reliability of the classification system, especially for edge cases identified in the notebook's clustering and regex phases.

---

## Folder Structure

1. **`training/`**:
   - Contains the Jupyter Notebook (`log_classification_training.ipynb`) for training models using SentenceTransformer and multiple classifiers (Random Forest, Naive Bayes, Logistic Regression).
   - Includes code for regex-based classification as part of the training pipeline.

2. **`clf_models/`**:
   - Stores the saved models, including the trained Random Forest (`random_forest.joblib`), Naive Bayes (`naive_bayes.joblib`), and Logistic Regression (`logistic_regression.joblib`) models, along with their SentenceTransformer embeddings.

3. **`files/`**:
   - This folder contains test CSV input files (`test.csv`, `test2.csv`, `test3.csv`).

4. **Root Directory**:
   - Contains the server script (`server.py`) implemented with FastAPI for serving model predictions.
   - Includes `locustfile.py` for load testing the system using Locust to simulate traffic and evaluate performance.

---

## Setup Instructions

1. **Install Dependencies**:
   Ensure you have Python installed on your system. Set up a virtual environment and install the required Python libraries by running the following commands:

   ```bash
   pip install -r requirements.txt
   ```
   
2. **Run the FastAPI Server**:
   To start the server, use the following command:

   ```bash
   uvicorn server:app --reload
   ```
   Access the API once the server is running at: `http://127.0.0.1:8000`


4. **Run Load Testing with Locust**:
   To simulate traffic and test the system's performance, use Locust by running:

   ```bash
   locust -f locustfile.py
   ```
   
   Access the Locust web interface at `http://127.0.0.1:8089` to configure and start the load test.

---

## Usage

Upload a CSV file containing logs to the FastAPI endpoint(Use Postman for testing) for classification. Ensure the file has the following columns:
- `source`
- `log_message`

The output will be a CSV file with an additional column `target_label`, which represents the classified label for each log entry.