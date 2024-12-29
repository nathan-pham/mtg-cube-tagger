import scrython
from bs4 import BeautifulSoup
import requests

def find_tags(set_code, collector_number):
    print(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")
    html_text = requests.get(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}").text
    print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    tags = soup.find_all('div', class_= 'tag-row')
    o_tags = []
    for tag in tags:
        o_tags.append(tag.text)
        print(tag.text)

print("Search Magic: The Gathering card")
query = input('> ')
print(f"Obtaining Oracle Tags for {query}...")

card = scrython.cards.Named(fuzzy=query)
set_code = card.set_code()
collector_number = card.collector_number()

find_tags(set_code, collector_number)