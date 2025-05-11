import requests
from bs4 import BeautifulSoup
import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

# Unified list of ticker names
tickers = [
    # Tech
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA", "ADBE",
    "CRM", "NOW", "INTC", "CSCO", "AMD", "PYPL", "ZM", "SQ", "NET",
    "SHOP", "PLTR", "TWLO",
    # Real Estate
    "PLD", "AMT", "CCI", "EQIX", "PSA", "O", "SPG", "AVB", "EXR",
    "WELL", "DLR", "EQR", "INVH", "MAA", "IRM", "CPT", "STWD",
    "BXP", "KIM", "VNO",
    # Energy
    "XOM", "CVX", "COP", "SLB", "EOG", "PXD", "OXY", "HAL", "BKR",
    "MPC", "PSX", "WMB", "LNG", "DVN", "KMI", "VLO", "CTRA", "NEE",
    "BP", "SHEL"
]

# Initialize DataFrame with columns
columns = ['ticker', 'datetime', 'title', 'source', 'link', 'top_sentiment', 'sentiment_score']
df = pd.DataFrame(columns=columns)

# Function to scrape news for a given ticker
def scrape_news(ticker, max_pages=60):
    global df
    counter = 0
    page = 1
    print(f"Scraping news for ticker: {ticker}")
    
    while page <= max_pages:
        url = f"https://markets.businessinsider.com/news/{ticker}-stock?p={page}"
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f"Failed to fetch page {page} for ticker {ticker} (Status code: {response.status_code}).")
            break
        
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        articles = soup.find_all('div', class_='latest-news__story')
        
        if not articles:
            print(f"No more articles found for ticker {ticker} on page {page}.")
            break
        
        for article in articles:
            datetime = article.find('time', class_='latest-news__date')
            title = article.find('a', class_='news-link')
            source = article.find('span', class_='latest-news__source')
            link = title.get('href', '') if title else ''
            
            row = {
                'ticker': ticker,
                'datetime': datetime.get('datetime', '') if datetime else '',
                'title': title.get_text(strip=True) if title else 'No Title',
                'source': source.get_text(strip=True) if source else 'Unknown Source',
                'link': link,
                'top_sentiment': '',
                'sentiment_score': 0
            }
            
            df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
            counter += 1
        
        print(f"Page {page} for ticker {ticker} processed. Articles scraped: {counter}")
        page += 1
    
    return counter

# Function for FinBERT sentiment analysis
def pipeline_method(payload):
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
    classifier = pipeline(
        "text-classification",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1
    )
    
    result = classifier(payload)
    return result

# Main execution
if __name__ == "__main__":
    total_articles = 0
    
    # Scrape news for all tickers
    for ticker in tickers:
        total_articles += scrape_news(ticker)
    
    print(f"\n{total_articles} articles scraped in total!")
    
    # Perform sentiment analysis on the scraped headlines
    counter = 0
    for index, row in df.iterrows():
        title = row['title']
        output = pipeline_method(title)
        df.at[index, 'top_sentiment'] = output[0]['label']
        df.at[index, 'sentiment_score'] = output[0]['score']
        counter += 1
        print(f"Processed row {counter}: {title}")
    
    # Save updated data with sentiment to CSV
    output_csv = "articles_with_sentiment.csv"
    df.to_csv(output_csv, index=False)
    print(f"Sentiment analysis completed for {counter} rows.")
    print(f"Data with sentiment saved to: {output_csv}")
