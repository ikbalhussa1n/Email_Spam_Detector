# 📩 Email Spam Detector (GRU + NLP + Streamlit)

A deep learning-based spam detection system that classifies messages as **Spam (1)** or **Ham / Not Spam (0)** using a GRU-based neural network built with TensorFlow/Keras and deployed using Streamlit.

---

## 🚀 Live Demo
Streamlit App: https://emailspamdetector-shevyhnrbwmmxulm3if5dx.streamlit.app/  
GitHub Repo: https://github.com/ikbalhussa1n/Email_Spam_Detector  

---

## 🧠 Project Overview
This project uses Natural Language Processing (NLP) and a Recurrent Neural Network (GRU) to detect spam messages. It includes text preprocessing, tokenization, padding, model training, and deployment as a web app.

---

## 📁 Project Files
- spam.csv → Dataset used for training  
- spam_detector_model.h5 → Trained GRU model  
- tokenizer.pickle → Tokenizer for text processing  
- main.py → Streamlit web app  
- requirements.txt → Dependencies  
- README.md → Project documentation  

---

## ⚙️ Tech Stack
Python, TensorFlow/Keras, GRU (RNN), NLP, Scikit-learn, NLTK, Streamlit

---

## 🔄 Pipeline

### 1. Data Preprocessing
- Lowercasing text
- Removing special characters
- Removing stopwords

### 2. Text Processing
- Tokenization (Keras Tokenizer)
- Converting text → sequences
- Padding sequences (max_len = 100)

### 3. Model Architecture
Embedding Layer → GRU (64 units) → Dense (Sigmoid)

### 4. Output
- 0 → Ham (Not Spam)
- 1 → Spam

---

## 📊 Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- ROC-AUC Score

---
## 🛠️ Setup Instructions

### Clone Repository
```bash
git clone https://github.com/ikbalhussa1n/Email_Spam_Detector.git
cd Email_Spam_Detector



Create Virtual Environment
python -m venv venv


Install Dependencies
pip install -r requirements.txt


▶️ Run App
streamlit run main.py

📷 Example

Input:
“Congratulations! You won a free iPhone. Click now to claim.”

Output:
🚨 Spam


👨‍💻 Author
Ikbal Hussain  
GitHub: https://github.com/ikbalhussa1n
