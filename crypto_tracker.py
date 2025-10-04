from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import os
import webbrowser

# Setup Chrome in headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-blink-features=AutomationControlled')

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open CoinMarketCap
    url = "https://coinmarketcap.com/"
    driver.get(url)
    WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.XPATH, '//tbody/tr')))

    # Get top 10 cryptocurrencies
    rows = driver.find_elements(By.XPATH, '//tbody/tr')[:10]

    coins, prices, changes, market_caps = [], [], [], []

    for row in rows:
        try:
            name = row.find_element(By.XPATH, './/td[3]//p').text
            price = row.find_element(By.XPATH, './/td[4]//span').text
            change = row.find_element(By.XPATH, './/td[5]/span').text
            market_cap = row.find_element(By.XPATH, './/td[7]//span').text

            coins.append(name)
            prices.append(price)
            changes.append(change)
            market_caps.append(market_cap)
        except Exception as e:
            print(f" Error processing row: {e}")

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create DataFrame
    df = pd.DataFrame({
        "Timestamp": [timestamp] * len(coins),
        "Coin": coins,
        "Price": prices,
        "24h Change": changes,
        "Market Cap": market_caps
    })

    # Save to CSV
    file_path = "crypto_price_data.csv"
    df.to_csv(file_path, mode='a', index=False, header=not os.path.exists(file_path))
    print(f" Data saved to '{file_path}'")

finally:
    driver.quit()

#  Open CoinMarketCap website in your default browser
webbrowser.open("https://coinmarketcap.com/")
print("Opened CoinMarketCap in your browser.")
