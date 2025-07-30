from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    label = "POSITIVE" if polarity > 0 else "NEGATIVE" if polarity < 0 else "NEUTRAL"
    return label, polarity
