import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # ⛔ Disable TensorFlow completely

from transformers import pipeline

# Load model once (global)
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    return result['label'].lower(), result['score']
