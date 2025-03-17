import pandas as pd

# Load the feature ranking and competitor data
feature_ranking = pd.read_csv("data/feature_ranking.csv")
competitor_data = pd.read_csv("data/competitor_features.csv")

# Merge the two datasets for a comparative analysis
comparison = pd.merge(feature_ranking, competitor_data, on="feature", how="left")

# Display the final comparison
print(comparison)

# Save the comparison to a file
comparison.to_csv("data/comparison_results.csv", index=False)

print("Competitive analysis complete and saved to 'comparison_results.csv'")
