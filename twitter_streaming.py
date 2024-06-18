import tweepy
from textblob import TextBlob
import pandas as pd
from datetime import datetime

# Twitter API credentials
api_key = '3k8hMelnKvcoJ2EsaormO0p1z'
api_secret_key = 'Jm4nQG7iH6Y96utxgB3l1QS0mz4csAWbsEqeYcj5EVSOg6kHpe'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJltuQEAAAAApzQSaf0p%2BBFBzhiLaGEzKuJfXWQ%3DPECzxvuiFQd3YR1k63BywcLQoFsZhVq3M2IZQSEB5YDyQVQI7f'

# Define a stream listener
class MyStreamListener(tweepy.StreamingClient):
    def __init__(self, bearer_token, time_limit=120):
        self.start_time = datetime.now()
        self.limit = time_limit
        self.tweets = []
        super(MyStreamListener, self).__init__(bearer_token)

    def on_tweet(self, tweet):
        if (datetime.now() - self.start_time).seconds < self.limit:
            tweet_text = tweet.text
            print(tweet_text)
            analysis = TextBlob(tweet_text)
            sentiment = analysis.sentiment.polarity
            self.tweets.append((datetime.now(), tweet_text, sentiment))
        else:
            self.disconnect()

    def on_error(self, status_code):
        if status_code == 420:
            return False

# Set up the streaming client
stream_listener = MyStreamListener(bearer_token, time_limit=120)  # Set time limit to 2 minutes

# Add rules to filter tweets by keywords
rules = [
    tweepy.StreamRule(value="keyword1"),
    tweepy.StreamRule(value="keyword2")
]

# Add rules to the streaming client
stream_listener.add_rules(rules)

# Start streaming
print("Collecting tweets...")
stream_listener.filter()

# After streaming, store tweets in DataFrame
df = pd.DataFrame(stream_listener.tweets, columns=['Time', 'Tweet', 'Sentiment'])

# Save DataFrame to CSV
df.to_csv('tweets.csv', index=False)
print("Stream ended. Saving tweets to tweets.csv...")
