# Email Classifier Project

This project is an AI-based email classifier that identifies and categorizes incoming emails as spam or not spam. The system integrates with a Gmail account using the IMAP protocol and performs email classification using a pre-trained machine learning model.

## Features
- Fetches emails from a Gmail inbox using the `imap-tools` library.
- Preprocesses email text using stemming and stopwords removal.
- Predicts whether an email is spam or not using a machine learning model.
- Automatically moves spam emails to the Spam folder in Gmail.

---

## Prerequisites

Before running the project, ensure you have the following installed:
- Python 3.6+
- Required Python libraries: `imap-tools`, `scikit-learn`, `nltk`, `re`, `pickle`

You also need:
1. **Model Files**:
   - `Model1.pkl` - Pre-trained classifier (e.g., Random Forest, Logistic Regression, etc.).
   - `Vectorizer1.pkl` - CountVectorizer fitted to the training dataset.
   - `stopwords.pkl` - A pickle file containing the stopwords list.

2. **Gmail Account**:
   - Make sure IMAP access is enabled in your Gmail account.
   - Create an app password (instead of using your account password) for enhanced security.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd email-classifier
