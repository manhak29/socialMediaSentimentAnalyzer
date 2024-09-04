from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Returns a value between -1 (negative) and 1 (positive)

if __name__ == '__main__':
    sample_text = "I love this product! It's amazing."
    sentiment = analyze_sentiment(sample_text)
    print(f'Sentiment score: {sentiment}')
