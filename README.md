# AISpamDetection
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



## Description
The `AISpamDetection` project is an AI-powered email spam detection tool. It leverages machine learning to analyze email content and predict whether it is spam (unsolicited) or ham (legitimate). The project utilizes a Streamlit web interface to provide an interactive user experience. Users can input email text and receive real-time analysis, along with probability scores indicating the likelihood of the email being spam or ham. Exploratory Data Analysis (EDA) is also integrated to visualize dataset characteristics, such as class distribution and word clouds, offering insights into the data used for training the model.



## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Important Links](#important-links)
- [Footer](#footer)



## Features
- **Email Spam Detection:** Detects spam emails using a pre-trained machine learning model. 📧
- **Streamlit Interface:** Provides an interactive web interface for email analysis. 💻
- **Exploratory Data Analysis (EDA):**  Includes visualizations such as bar charts for class distribution and word clouds for spam and ham emails. 📊
- **Text Preprocessing:** Implements text cleaning using techniques like removing punctuation, stop words, and stemming. 🧹
- **Probability Scores:** Displays probability scores for both spam and ham predictions. 💯
- **User Input:** Allows users to input custom email text for real-time analysis. ✍️



## Tech Stack
- **Primary Language:** Python 🐍
- **Frameworks:** Streamlit, scikit-learn
- **Libraries:** pandas, matplotlib, nltk, joblib, wordcloud



## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/HAM0909/AISpamDetection.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd AISpamDetection
   ```
3. **Install Dependencies:**
   While no explicit dependency file is provided, the `app.py` script imports several libraries. Install them using pip:
   ```bash
   pip install streamlit pandas scikit-learn matplotlib nltk joblib wordcloud
   ```
4. **Download NLTK Stopwords:**
   Run the following lines in a Python environment to download necessary NLTK resources:
   ```python
   import nltk
   nltk.download('stopwords')
   ```
5. **Place the trained model:**
Place `best_model.pkl` in the same directory as `app.py`. If you don't have the file you need to train and save your own
6. **Place the Vectorizer:**
Place `vectorizer.pkl` in the same directory as `app.py`. If you don't have the file you need to train and save your own


7. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```



## Usage
This project can be used to:

- Analyze email content to detect spam.
- Visualize and explore email datasets.
- Test and evaluate spam detection models.
- Integrate spam detection functionality into other applications.



## How to Use
1. **Access the Streamlit App:**
   After running `streamlit run app.py`, access the app in your web browser at the provided local URL (usually `http://localhost:8501`).
2. **Explore the EDA Tab:**
   Click on the '🔍 Analyse Exploratoire' tab to view visualizations of the email dataset, including class distribution and word clouds.
3. **Use the Spam Detection Tab:**
   Click on the '🤖 Détection Spam' tab.
   Enter the email content in the text area.
   Click the 'Analyser' button.
   View the prediction result and probability scores displayed below the input area.
   ```text
   ✍️ Entrez le contenu de l'email : Get your free iPhone now!
   Analyser
   🚨 L'email est probablement un **SPAM**.
   Probabilité Spam : 99.99%
   Probabilité Ham : 0.01%
   ```



## Project Structure
```
AISpamDetection/
├── AIspamEmail.ipynb
├── app.py
└── README.md
```

- `AIspamEmail.ipynb`: Jupyter Notebook (content not available).
- `app.py`: The main Streamlit application script containing the email spam detection logic.
- `README.md`: The project's README file (this document).



## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Submit a pull request.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



## Important Links
- **Repository Link:** [https://github.com/HAM0909/AISpamDetection](https://github.com/HAM0909/AISpamDetection)



## Footer
- Repository: [AISpamDetection](https://github.com/HAM0909/AISpamDetection)
- Author: HAM0909

⭐️ Star this repository on GitHub if you found it helpful! Fork it to contribute and open issues for any problems or suggestions. 📧
