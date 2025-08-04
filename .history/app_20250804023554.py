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
    text = text.lower()
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    tokens = text.split()
    tokens = [w for w in tokens if w not in stop_words]
    tokens = [stemmer.stem(w) for w in tokens]
    return ' '.join(tokens)

# Charger les données pour EDA
@st.cache_data
def load_data():
    return pd.read_csv("DataSet_Emails.csv")

df = load_data()

# Prétraitement des textes si pas déjà faits
if 'clean_text' not in df.columns:
    df['clean_text'] = df['text'].apply(preprocess_text)

# Charger le modèle entraîné et le vectorizer
model = joblib.load("best_model.pkl")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['clean_text'])  # Doit matcher avec entraînement

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
