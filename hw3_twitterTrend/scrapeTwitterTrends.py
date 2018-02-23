import requests
from bs4 import BeautifulSoup as bs

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_trends():
    url = "https://trends24.in/canada"
    response = requests.get(url, headers=headers)
    html = response.text
    soup = bs(html, "html.parser")

    trends = soup.select('.trend-card__list a')

    with open("twitter_trend_CA2.txt", "w") as outfile:
        for trend in trends:
            outfile.write(trend.text + "\n")


get_trends()
