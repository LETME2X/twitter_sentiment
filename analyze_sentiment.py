import pandas as pd
import matplotlib.pyplot as plt

# Load the tweets
df = pd.read_csv('tweets.csv')

# Convert 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Plot the sentiment over time
plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Sentiment'], marker='o')
plt.title('Sentiment Analysis of Tweets Over Time')
plt.xlabel('Time')
plt.ylabel('Sentiment')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
