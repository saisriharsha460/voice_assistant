from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB


def train_sentiment_classifier():
    sentences = [
        "I love this chatbot.",
        "This is a fantastic experience.",
        "I'm not happy with the response.",
        "This is terrible.",
    ]
    sentiments = ["positive", "positive", "negative", "negative"]

    senti_vectorizer = TfidfVectorizer()
    X = senti_vectorizer.fit_transform(sentences)
    y = sentiments

    senti_classifier = MultinomialNB()
    senti_classifier.fit(X, y)

    return senti_vectorizer, senti_classifier

def train_music_classifier():
    music_commands = ["play music", "play a song", "start music"]
    music_labels = [1, 2, 3]  
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(music_commands)
    y = music_labels

    classifier = SVC(kernel='linear', C=1.0)
    classifier.fit(X, y)

    return vectorizer, classifier

def train_browser_classifier():
    browser_commands = ["open a browser", "launch web browser", "start a browser"]
    browser_labels = [1, 2, 3]  

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(browser_commands)
    y = browser_labels

    classifier = SVC(kernel='linear', C=1.0)
    classifier.fit(X, y)

    return vectorizer, classifier





