import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_dataset.csv")

# Convert price into numbers
df["Price"] = df["Price"].str.extract(r"(\d+\.\d+)")[0].astype(float)

# Convert ratings into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Basic analysis
print("===== DATA ANALYSIS =====")
print("Total Books:", len(df))
print("Average Price: £", round(df["Price"].mean(), 2))
print("Minimum Price: £", round(df["Price"].min(), 2))
print("Maximum Price: £", round(df["Price"].max(), 2))
print("Average Rating:", round(df["Rating"].mean(), 2))

# Rating count
rating_counts = df["Rating"].value_counts().sort_index()

print("\n===== RATING COUNT =====")
print(rating_counts)

# Chart 1: Rating distribution
plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")
plt.title("Books by Rating")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# Chart 2: Price distribution
plt.figure(figsize=(8, 5))
df["Price"].plot(kind="hist", bins=10)
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

print("\nAnalysis completed successfully!")
import matplotlib.pyplot as plt

plt.figure()
plt.hist(df["Price"], bins=10)
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.title("Price Distribution of Books")
plt.savefig("price_distribution.png")
plt.show()