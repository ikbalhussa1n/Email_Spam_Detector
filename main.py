import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import pickle
import re
from nltk.corpus import stopwords
import nltk

# =========================
# NLTK SETUP (safe for Streamlit)
# =========================
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

# =========================
# LOAD MODEL + TOKENIZER
# =========================
model = tf.keras.models.load_model('spam_detector_model.h5')

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# =========================
# CONFIG
# =========================
max_len = 100

# =========================
# PREPROCESSING
# =========================
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)

    words = text.split()
    words = [w for w in words if w not in stop_words]

    text = " ".join(words)

    sequence = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequence, maxlen=max_len, padding='post')

    return padded

# =========================
# STREAMLIT UI
# =========================
st.title("📩 Spam Message Detector")
st.write("Enter a message and the model will predict if it's Spam or Ham.")

user_input = st.text_area("Your message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        processed_input = preprocess_text(user_input)
        prediction = model.predict(processed_input)

        score = prediction[0][0]
        st.write(f"Raw prediction score: {score:.4f}")

        if score > 0.5:
            st.error("🚨 This message is SPAM!")
        else:
            st.success("✅ This message is NOT SPAM (HAM)")