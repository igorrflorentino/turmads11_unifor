from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests

HTML = requests.get("http://quotes.toscrape.com/")

# bs = BeautifulSoup(HTML.text, "html.parser")
bs = BeautifulSoup(HTML.text, "lxml")

print(bs.find_all("span")[2].text)
