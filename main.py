import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

def fetch_comments(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    comments = soup.find_all(class_='comment')
    return [comment.get_text() for comment in comments]

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def main():
    url = 'https://example.com/comments'  # Replace with the actual URL
    comments = fetch_comments(url)
    
    sentiment_scores = [analyze_sentiment(comment) for comment in comments]
    
    # Print sentiment analysis results
    for i, score in enumerate(sentiment_scores):
        print(f'Comment {i+1} sentiment score: {score}')

if __name__ == '__main__':
    main()
