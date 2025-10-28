import praw

reddit = praw.Reddit(
    client_id="Enter your client ID here",
    client_secret="Enter your client secret here",
    user_agent="social_media_analytics by u/YourRedditUsername"
)

reddit.read_only = True
subreddit = reddit.subreddit("RX100")
for post in subreddit.hot(limit=5):
    print(post.title, post.score, post.num_comments)


import pandas as pd
import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Reddit API fetch
reddit = praw.Reddit(
    client_id="Enter your client ID here",
    client_secret="Enter your client secret here",
    user_agent="social_media_analytics by u/YourRedditUsername"
)

reddit.read_only = True
subreddit = reddit.subreddit("RX100")
posts = []

for post in subreddit.hot(limit=5):  
    posts.append([post.title, post.score, post.num_comments])

# Save to CSV
df = pd.DataFrame(posts, columns=["title", "score", "num_comments"])
df.to_csv("reddit_posts.csv", index=False)
print("Saved top posts to reddit_posts.csv")

# Sentiment Analysis
analyzer = SentimentIntensityAnalyzer()
df["sentiment"] = df["title"].apply(lambda x: analyzer.polarity_scores(str(x))["compound"])

print(df.head())

