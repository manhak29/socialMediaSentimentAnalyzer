import requests
from bs4 import BeautifulSoup

def fetch_comments(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # This is a placeholder; you'll need to adjust the selector based on the actual site structure
    comments = soup.find_all(class_='comment')
    
    return [comment.get_text() for comment in comments]

if __name__ == '__main__':
    url = 'https://example.com/comments'  # Replace with the actual URL
    comments = fetch_comments(url)
    for comment in comments:
        print(comment)
