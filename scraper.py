import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Get website data
response = requests.get(url)

# Read HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Empty list to store data
data = []

# Extract book information
for book in books:

    title = book.h3.a["title"]

    price = book.find(
        "p",
        class_="price_color"
    ).text

    rating = book.find(
        "p",
        class_="star-rating"
    )["class"][1]

    data.append({
        "Book Name": title,
        "Price": price,
        "Rating": rating
    })

# Convert data into DataFrame
df = pd.DataFrame(data)

# Display data
print(df)

# Save as CSV
df.to_csv("books_dataset.csv", index=False)

print("\nDataset created successfully!")