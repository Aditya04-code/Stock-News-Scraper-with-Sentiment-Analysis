# MLH Stock Sentiment Analyzer

## Overview
Welcome to the **MLH Stock Sentiment Analyzer**, a Python-based project developed by Aditya for a Major League Hacking (MLH) submission. This tool scrapes news headlines for a curated list of stock tickers from the Tech, Real Estate, and Energy sectors, performs sentiment analysis using the FinBERT model, and outputs the results to a CSV file. The project aims to provide insights into market sentiment based on recent news articles, making it valuable for financial analysis and research.

## Features
- **Web Scraping**: Collects news articles for 60 stock tickers from Business Insider's markets section.
- **Sentiment Analysis**: Uses the FinBERT model to classify headlines as positive, negative, or neutral with confidence scores.
- **Comprehensive Data**: Extracts ticker, datetime, title, source, and link for each article, alongside sentiment results.
- **Output**: Saves results to `articles_with_sentiment.csv` for easy analysis.
- **GPU Support**: Leverages GPU acceleration for faster sentiment analysis if available.

## Prerequisites
- Python 3.8 or higher
- Internet connection (for web scraping and downloading the FinBERT model)
- Optional: GPU for faster sentiment analysis with PyTorch

## Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Aditya04-code/mlh-stock-sentiment-analyzer.git
   cd mlh-stock-sentiment-analyzer
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Install the required Python packages listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` contains:
   ```
   requests
   beautifulsoup4
   pandas
   transformers
   torch
   ```

## Usage
1. **Run the Script**:
   Execute the main script to scrape news and perform sentiment analysis:
   ```bash
   python news_scraper_with_sentiment.py
   ```

2. **What It Does**:
   - Scrapes up to 60 pages of news articles per ticker from Business Insider.
   - Analyzes the sentiment of each headline using FinBERT.
   - Saves the results to `articles_with_sentiment.csv` in the project directory.

3. **Output Format**:
   The `articles_with_sentiment.csv` file includes:
   - `ticker`: Stock ticker symbol (e.g., AAPL, XOM)
   - `datetime`: Article publication date and time
   - `title`: News headline
   - `source`: News source (e.g., Reuters, Bloomberg)
   - `link`: URL to the full article
   - `top_sentiment`: Sentiment label (positive, negative, neutral)
   - `sentiment_score`: Confidence score (0 to 1)

4. **Example Output**:
   ```csv
   ticker,datetime,title,source,link,top_sentiment,sentiment_score
   AAPL,2025-05-10T12:00:00,Apple Announces New iPhone,Reuters,https://example.com,positive,0.87
   XOM,2025-05-10T13:00:00,Oil Prices Fall Amid Oversupply,Bloomberg,https://example.com,negative,0.76
   ```

5. **Testing Tip**:
   To reduce runtime during testing, edit `news_scraper_with_sentiment.py` and set `max_pages=5` in the `scrape_news` function.

## File Structure
```
mlh-stock-sentiment-analyzer/
├── news_scraper_with_sentiment.py  # Main script for scraping and sentiment analysis
├── requirements.txt                # Python dependencies
├── articles_with_sentiment.csv     # Output CSV (generated after running)
├── README.md                       # This documentation
├── LICENSE                         # MIT License file
└── .gitignore                      # Ignores virtual env, CSV, and pycache
```

## Example Console Output
When you run the script, you’ll see progress updates like:
```
Scraping news for ticker: AAPL
Page 1 for ticker AAPL processed. Articles scraped: 10
...
No more articles found for ticker AAPL on page 20.
...
Processed row 1: Apple Announces New iPhone
...
Sentiment analysis completed for 600 rows.
Data with sentiment saved to: articles_with_sentiment.csv
```

## Important Notes
- **Runtime**: Scraping 60 pages per ticker and analyzing sentiments can take significant time. A GPU can speed up the FinBERT model.
- **Web Scraping Limits**: Excessive scraping may trigger rate limits on Business Insider. If issues arise, add a delay (e.g., `time.sleep(1)`) in the `scrape_news` function.
- **Model Download**: The FinBERT model is downloaded automatically on the first run, requiring an internet connection.
- **Output File**: The `articles_with_sentiment.csv` file is overwritten each time the script runs. Back up previous results if needed.

## Contributing
We welcome contributions to improve this project! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please adhere to PEP 8 style guidelines and update documentation as needed.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Created for a Major League Hacking (MLH) hackathon submission.
- Powered by the FinBERT model from ProsusAI for sentiment analysis.
- Data sourced from Business Insider’s markets news section.

## Contact
For questions, bug reports, or suggestions, please open an issue on this GitHub repository or contact Aditya via GitHub.

---

*Built with ❤️ for MLH*
