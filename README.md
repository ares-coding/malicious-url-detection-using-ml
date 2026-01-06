🔐 Malicious URL Detection Using Machine Learning

📌 Project Overview

This project focuses on detecting malicious URLs (e.g., phishing, malware, scam links) using Machine Learning techniques.
Instead of relying on webpage content, the system analyzes URL-based features such as length, structure, entropy, and suspicious patterns to classify URLs as Benign or Malicious.

The goal is to demonstrate how ML can be applied to cybersecurity problems in a lightweight, explainable, and practical manner.

🎯 Objectives

Build an ML-based system to classify URLs as malicious or benign

Apply feature engineering on raw URL strings

Compare multiple ML algorithms

Evaluate model performance using standard metrics

Provide a clean, reproducible ML pipeline

📂 Dataset Description

The dataset consists of URLs labeled into two classes:

0 – Benign URLs

1 – Malicious URLs

Each URL is transformed into numerical features using a custom feature extraction process.

📌 Datasets may come from public sources such as phishing URL repositories, malware URL feeds, or combined open datasets.

🧠 Feature Engineering

The model does not inspect webpage content. Instead, it extracts meaningful characteristics directly from URLs:

Feature	Description
URL Length	Total number of characters
Number of Dots (.)	Indicates multiple subdomains
Number of Digits	Randomized or obfuscated URLs
Presence of IP Address	Common in malicious URLs
Special Characters Count	@, -, ?, =, _
HTTPS Usage	Indicates encrypted connection
Entropy Score	Measures randomness
Suspicious Keywords	e.g., login, verify, bank, secure

These features allow the model to remain fast, explainable, and scalable.

🤖 Machine Learning Models

The following models are trained and evaluated:

Logistic Regression (baseline)

Support Vector Machine (SVM) ⭐ Primary Model

Random Forest Classifier

SVM is emphasized due to its strong performance on high-dimensional feature spaces.

📊 Evaluation Metrics

Model performance is evaluated using:

Accuracy

Precision

Recall

F1-score

Confusion Matrix

These metrics ensure a balanced evaluation, especially for security-related classification tasks.

🧪 Workflow

Load and preprocess dataset

Extract URL-based features

Split data into training and testing sets

Train ML models

Evaluate performance

Save trained models for reuse

🛠️ Tech Stack

Python

Scikit-learn

NumPy

Pandas

Matplotlib

Regular Expressions (re)

🚀 Possible Enhancements

Add real-time URL checking using a web interface (Streamlit / Flask)

Include deep learning models for comparison

Integrate blacklist-based hybrid detection

Deploy as a browser extension or API service


👨‍💻 Author
Ares Coding

Software Developer & AI Engineer

Focused on Machine Learning, Computer Vision, and Security Systems

📄 License

This project is licensed under the MIT License — free to use with attribution.

## Status
- Feature extraction completed
- SVM baseline model trained successfully
