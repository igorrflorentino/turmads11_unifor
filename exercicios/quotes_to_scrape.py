from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests

HTML = requests.get("http://quotes.toscrape.com/")

# soup = BeautifulSoup(HTML.text, "html.parser")
soup = BeautifulSoup(HTML.text, "lxml")

# Exercicio 1
print(f"Título da página: {soup.find_all('h1')[0].text.strip()}\n")

# Exercicio 2
print(f"Primeira citação: {soup.find_all('span', class_='text')[0].text.strip()}\n")

# Exercicio 3
print(f"Autor da citação: {soup.find_all('small', class_='author')[0].text.strip()}\n")

# Exercicio 4
print(f"Tags da citação: {[tag.text.strip() for tag in soup.find('div', class_='tags').find_all('a', class_='tag')]}\n")

# Exercicio 5
print(f"Total de quotes: {len(soup.find_all('div', class_='quote'))}\n")

# Exercicio 6
print(f"Autores unicos: {sorted(set(author.text.strip() for author in soup.find_all('small', class_='author')))}\n")

# Exercicio 7
print(f"Quote Mais Longa: {max(soup.find_all('span', class_='text'), key=len).text.strip()}\n")

# Exercicio 8
print(f"Citações do autor 'Albert Einstein': {[quote.find('span', class_='text').text.strip() for quote in soup.find_all('div', class_='quote') if quote.find('small', class_='author').text.strip() == 'Albert Einstein']}\n")

# Exercicio 9
from collections import Counter
tags = [tag.text.strip() for tag in soup.find_all('a', class_='tag')]
print(f"Top 5 Tags: {Counter(tags).most_common(5)}\n")

# Exercicio 10
print(f"Links de navegação: {[link['href'] for link in soup.find('div', class_='row header-box').find_all('a')]}\n")