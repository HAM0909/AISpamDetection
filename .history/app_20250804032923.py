import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Téléchargements NLTK (à faire une fois)
nltk.download('stopwords')

# Prétraitement du texte (doit correspondre à celui utilisé dans l'entraînement)
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

def preprocess_text(text):
    import string
    import re
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r'<.*?>', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    words = [stemmer.stem(w) for w in words]
    return ' '.join(words)


# Charger les données pour EDA
import os

@st.cache_data
def load_data():
    path = os.path.join(os.path.dirname(__file__), "DataSet_Emails.csv")
    return pd.read_csv(path)


df = load_data()

# Prétraitement des textes si pas déjà faits
if 'clean_text' not in df.columns:
    df['text'] = df['text'].fillna('')
    df['clean_text'] = df['text'].apply(preprocess_text)

# Charger le modèle entraîné et le vectorizer
model = joblib.load("best_model.pkl")
  # Doit matcher avec entraînement

# 🎨 Interface Streamlit
st.title("📧 Détecteur de Spam - BMSecurity AI")

# 📊 Onglets : Analyse / Prédiction
tabs = st.tabs(["🔍 Analyse Exploratoire", "🤖 Détection Spam"])

# --- 🧪 Onglet EDA ---
with tabs[0]:
    st.header("Exploration du Dataset")
    st.write("**Répartition des classes (Ham vs Spam)**")
    st.bar_chart(df['label_text'].value_counts())

    # WordCloud Ham & Spam
    spam_words = ' '.join(df[df['label_text'] == 'spam']['clean_text'])
    ham_words = ' '.join(df[df['label_text'] == 'ham']['clean_text'])

    st.write("**Nuage de mots - Spam**")
    wc_spam = WordCloud(width=800, height=400).generate(spam_words)
    st.image(wc_spam.to_array(), use_column_width=True)

    st.write("**Nuage de mots - Ham**")
    wc_ham = WordCloud(width=800, height=400).generate(ham_words)
    st.image(wc_ham.to_array(), use_column_width=True)

# --- 🧠 Onglet Détection Spam ---
with tabs[1]:
    st.header("Testez un Email")
    user_input = st.text_area("✍️ Entrez le contenu de l'email :", height=200)

    if st.button("Analyser"):
        if user_input.strip() == "":
            st.warning("Veuillez saisir un texte à analyser.")
        else:
            clean_input = preprocess_text(user_input)
            input_vector = vectorizer.transform([clean_input])
            prediction = model.predict(input_vector)[0]
            proba = model.predict_proba(input_vector)[0]

            if prediction == 1:
                st.error(f"🚨 L'email est probablement un **SPAM**.")
            else:
                st.success(f"✅ L'email est probablement **légitime (HAM)**.")

            st.write(f"**Probabilité Spam : {proba[1]*100:.2f}%**")
            st.write(f"**Probabilité Ham : {proba[0]*100:.2f}%**")

model_path = os.path.join(os.path.dirname(__file__), "best_model.pkl")

if not os.path.exists(model_path):
    st.error("❌ Fichier 'best_model.pkl' introuvable. Veuillez l'entraîner et le sauvegarder.")
    st.stop()

model = joblib.load(model_path)