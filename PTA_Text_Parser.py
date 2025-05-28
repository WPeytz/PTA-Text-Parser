import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re

# Step 1: Fetch the HTML content
url = "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A22011A0514(01)"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract paragraphs from the document
paragraphs = soup.find_all('p')  # or 'div', depending on structure
data = []
current_article = "Unspecified"  # Initialize with a default

for p in paragraphs:
    text = p.get_text(strip=True)
    if "Article" in text:  # crude but good for demo
        current_article = text
    elif len(text) > 30:  # ignore junk
        data.append({'Article': current_article, 'Text': text})

# Step 3: Convert to DataFrame
df = pd.DataFrame(data)
# Filter out rows that don't have a real article reference
df = df[df['Article'].str.match(r'^Article\s+\d+(\.\d+)?')]

# Step 4: Export
df.to_csv("pta_rules_of_origin.csv", index=False)
print("Saved rules to CSV.")

# Step 5: Analyze the text data
# Word count per row
df['WordCount'] = df['Text'].apply(lambda x: len(x.split()))

# Total word count per article
word_counts = df.groupby('Article')['WordCount'].sum().sort_values(ascending=False)

# Keyword analysis
# Keyword analysis using regex to catch variations
keywords = {
    'originating': r'\borigin\w*\b',
    'cumulation': r'\bcumulat\w*\b',
    'tolerance': r'\btoleranc\w*\b',
    'HS': r'\bHS\b|\bHarmonized System\b|\bheading\b'
}

for name, pattern in keywords.items():
    df[f'{name}_count'] = df['Text'].str.lower().apply(lambda x: len(re.findall(pattern, x)))

keyword_totals = df[[f'{name}_count' for name in keywords]].sum()

print("\nTop 5 Longest Articles (by word count):\n", word_counts.head())
print("\nKeyword Totals:\n", keyword_totals)

# Step 6: Visualize the results (using full Article names)

# Recalculate word counts using full Article names (no collapsing)
accurate_word_counts = df.groupby('Article')['WordCount'].sum().sort_values(ascending=False)

# Optional: Only take top N articles for clarity
top_n = 15
accurate_word_counts = accurate_word_counts.head(top_n)

# Plot word count per full Article name
plt.figure(figsize=(12,6))
accurate_word_counts.plot(kind='bar')
plt.title("Word Count per Article (Full Titles)")
plt.ylabel("Word Count")
plt.xlabel("Article")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("wordcount_per_article.png")

# Keyword bar chart (leave as-is)
plt.figure(figsize=(6,4))
keyword_totals.plot(kind='bar', color='skyblue')
plt.title("Keyword Frequency in PTA Rules of Origin")
plt.ylabel("Occurrences")
plt.tight_layout()
plt.savefig("keyword_frequencies.png")

# Show plots
plt.show()


