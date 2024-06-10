from bs4 import BeautifulSoup
import requests
import re



response = requests.get("https://en.wikipedia.org/wiki/Bristlecone_pine")
print(response.text)


def get_html(url, path):
        response = requests.get(url)
        with open(path, 'w', encoding='utf=8') as f:
                f.write(response.text)
get_html("https://en.wikipedia.org/wiki/Bristlecone_pine", 'E:\BD-Code\Zenva\Intermediate-Web_Scraping/Brislecone_pine.html')