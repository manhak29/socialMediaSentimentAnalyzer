import matplotlib.pyplot as plt

def plot_sentiments(sentiment_scores):
    plt.hist(sentiment_scores, bins=20, edgecolor='black')
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == '__main__':
    sample_scores = [0.5, -0.3, 0.1, 0.7, -0.6]  # Replace with actual sentiment scores
    plot_sentiments(sample_scores)
