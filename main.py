import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_gold_silver_rates(url):
    """
    Scrapes gold and silver rates from the specified URL and displays the rates along with the rate differences.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        None
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    find = soup.findAll('font', {"class": "txt-clr"})
    rate_dict = []

    for i in find:
        rate_dict.append((i.getText().strip()))

    my_dict = []

    for i in range(0, len(rate_dict), 5):
        my_dict.append(
            {"Day": rate_dict[i], "Rate": int(float(rate_dict[i + 1:i + 4][0]))})

    df = pd.DataFrame.from_dict(my_dict)
    df['Difference'] = df['Rate'].astype(int).diff(periods=-1).fillna(0)

    print(df.to_string())


# Usage example
url = "https://www.livechennai.com/gold_silverrate.asp"
scrape_gold_silver_rates(url)
