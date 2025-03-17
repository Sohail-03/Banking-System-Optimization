import pandas as pd
import matplotlib.pyplot as plt

# Load the feedback with sentiment data
feedback_data = pd.read_csv("data/feedback_with_sentiment.csv")

# Rank features based on sentiment and frequency of mentions
feature_ranking = feedback_data.groupby("feature").agg(
    avg_sentiment=("sentiment", "mean"),
    count=("feature", "count")
).reset_index()

# Sort features by sentiment and frequency
feature_ranking = feature_ranking.sort_values(by=["avg_sentiment", "count"], ascending=False)

# Visualize the feature rankings
plt.figure(figsize=(10, 6))
plt.barh(feature_ranking["feature"], feature_ranking["avg_sentiment"], color='skyblue')
plt.xlabel('Average Sentiment Score')
plt.ylabel('Features')
plt.title('Feature Recommendations Based on Customer Feedback')
plt.show()

# Save the feature ranking to a file
feature_ranking.to_csv("data/feature_ranking.csv", index=False)

print("Feature ranking complete and saved to 'feature_ranking.csv'")
