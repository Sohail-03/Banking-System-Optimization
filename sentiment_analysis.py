import pandas as pd
from textblob import TextBlob

# Load the customer feedback dataset
feedback_data = pd.read_csv("data/customer_feedback.csv")

# Function to get sentiment score from comments
def get_sentiment(comment):
    return TextBlob(comment).sentiment.polarity

# Apply sentiment analysis
feedback_data['sentiment'] = feedback_data['comments'].apply(get_sentiment)

# Save the data with sentiment scores
feedback_data.to_csv("data/feedback_with_sentiment.csv", index=False)

print("Sentiment analysis complete and saved to 'feedback_with_sentiment.csv'")
