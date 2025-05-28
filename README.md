## 📘 PTA Text Parser

This project extracts, processes, and analyzes legal text from a Preferential Trade Agreement (PTA) — specifically the EU–South Korea Free Trade Agreement. The focus is on the Rules of Origin section, which defines the criteria for goods to qualify as originating under the agreement.

---

## 🚀 What It Does

- Scrapes HTML content from the EU’s legal document portal using `requests` and `BeautifulSoup`
- Parses individual paragraphs and assigns them to legal articles
- Cleans and filters to ensure only actual articles (e.g., “Article 3”) are retained
- Counts words per article to identify verbosity champions
- Searches for keywords related to trade policy using regex (e.g., “originating”, “cumulation”)
- Visualizes:
  - Word counts per article
  - Keyword frequency

---

## 📂 Files

- `PTA_Text_Parser.py` – Main script (scraping, parsing, analyzing, plotting)
- `pta_rules_of_origin.csv` – Cleaned dataset of article-paragraph mappings
- `wordcount_per_article.png` – Bar chart of top 15 longest articles
- `keyword_frequencies.png` – Bar chart of keyword frequency in text
- `pta_explorer.py` – Streamlit app for interactive exploration

---

## 🔍 Example Output

### Top 5 Longest Articles:

Article 3    1223 words
Article 6     999 words
Article 5     901 words
Article 1     899 words
Article 2     814 words

### Keyword Occurrences (with regex):
originating: 17
cumulation: 1
tolerance: 0
HS: 0

---

## ⚙️ How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourname/PTA-Text-Parser.git
cd PTA-Text-Parser
```
2.	Install requirements (optional: use a virtual environment):

```bash
pip install -r requirements.txt
```
3.	Run the parser:
```bash
python PTA_Text_Parser.py
```
🧠 Future Improvements
	•	Tag paragraphs by type: definition, procedure, exception
	•	Add section-level parsing beyond “Article X”
	•	Expand keyword dictionary using NLP techniques
	•	Integrate Streamlit UI for interactive exploration

💡 Why This Project?

Because someone had to read the legalese so you didn’t have to — and I wanted to prove I can extract meaningful structure and analysis from complex text data using Python and beautiful soup.