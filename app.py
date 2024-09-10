from imap_tools import MailBox
import pickle
import re
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer

MAIL_PASSWORD = "your_password_here"
MAIL_USERNAME = "dhureen.project@gmail.com"

with open('Model1.pkl', 'rb') as f:
    classifier = pickle.load(f)
    
with open('Vectorizer1.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('stopwords.pkl', 'rb') as f:
    stopwords = pickle.load(f)

def preprocess_email(email_text):
    ps = PorterStemmer()
    email = re.sub('[^a-zA-Z]', ' ', email_text)
    email = email.lower()
    email = email.split()
    email = [ps.stem(word) for word in email if not word in stopwords]
    return ' '.join(email)

def predict_email(email_text):
    processed_email = preprocess_email(email_text)
    email_features = vectorizer.transform([processed_email]).toarray()
    return classifier.predict(email_features)

with MailBox("imap.gmail.com").login(MAIL_USERNAME, MAIL_PASSWORD, "Inbox") as mb:
    # for folder in mb.folder.list():
    #     print(folder.name)
    for msg in mb.fetch(limit=10, reverse=True, mark_seen=False):
        print(msg.text)
        spam = bool(predict_email(msg.text)[0])
        if spam:
            print("spam")
            mb.move(msg.uid, '[Gmail]/Spam')
        else:
            print("not spam")
        # print("Prediction:", predict_email(msg.text))
        print("-------------------------------------")
        # print(msg.subject, msg.uid, msg.from_)
        # print(predict_email(msg.text))
        # if msg.from_ == 'dhureen.project@gmail.com':
        #     mb.move(msg.uid, '[Gmail]/Spam')

    # mb.move("123", "Drafts")