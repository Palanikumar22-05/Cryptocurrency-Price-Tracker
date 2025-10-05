🪙 Cryptocurrency Price Tracker

A mini web scraping project that tracks the top 10 cryptocurrencies from CoinMarketCap using Python + Selenium, and saves the data to a CSV file.  

Repository: Palanikumar22-05 / Cryptocurrency-Price-Tracker

---

 🔍 Project Description

- Scrapes live data (name, price, 24h change, market cap) for the top 10 cryptocurrencies.  
- Runs in headless mode (no browser UI displayed).  
- Appends data with timestamp to a CSV (so you can collect historical data).  
- Opens the CoinMarketCap site in your browser after scraping for easy viewing.

---

 🛠 Tech Stack & Dependencies

- Python  
- Libraries:
  - `selenium`
  - `webdriver-manager`
  - `pandas`  
- Browser: Chrome (headless via WebDriver)  

---

📦 Installation & Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/Palanikumar22-05/Cryptocurrency-Price-Tracker.git
   cd Cryptocurrency-Price-Tracker

2.Install the required dependencies:

pip install -r requirements.txt

 Usage

Run the script:
python IMDB_Movie_rating.py


What happens:

IMDb’s Top 250 page is opened (in Chrome)
Movie title, year, and rating are scraped
Data is saved as imdb_top_250_YYYYMMDD_HHMMSS.csv
A preview of the top 15 entries is printed
