# Task 3 : Data Visualization
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("quotes.csv")

# Top authors ka graph
top_authors = df['Author'].value_counts().head(5)

plt.figure(figsize=(7,5))
sns.barplot(x=top_authors.values, y=top_authors.index, palette="viridis")
plt.title("Top 5 Authors with Most Quotes")
plt.xlabel("Number of Quotes")
plt.ylabel("Author")
plt.show()

# Quote length distribution
plt.figure(figsize=(7,5))
sns.histplot(df['Quote_Length'], bins=10, kde=True)
plt.title("Distribution of Quote Lengths")
plt.xlabel("Length of Quotes")
plt.ylabel("Frequency")
plt.show()
