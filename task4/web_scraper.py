import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://www.bbc.com/news"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("\n BBC NEWS HEADLINES:\n")

    headlines = soup.find_all("h3")

    count = 0
    for headline in headlines:
        text = headline.get_text().strip()
        if text:
            count += 1
            print(f"{count}. {text}")

    if count == 0:
        print("No headlines found!")

except requests.exceptions.RequestException as e:
    print("Error fetching the website:", e)
