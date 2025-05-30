from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import nltk

# Download required data (only needed once)
nltk.download('vader_lexicon')

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "positive 🥰"
    elif sentiment < 0:
        return "negative 😭"
    else:
        return "neutral 👍"

def analyze_sentiment_polarity(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)['compound']

    if sentiment > 0.05:
        return "positive 🥰"
    elif sentiment < -0.05:
        return "negative 😭"
    else:
        return "neutral 👍"

def analyze_input():
    text = input("Enter the text to be analysed: ")
    print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")
    print(f"VADER Sentiment: {analyze_sentiment_polarity(text)}")

analyze_input()
