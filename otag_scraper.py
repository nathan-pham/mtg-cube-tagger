import scrython
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chromedriver_path = '/usr/bin/chromedriver'
service = Service(chromedriver_path)


def find_tags(set_code, collector_number):
    print(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")

    driver = webdriver.Chrome(service=service)
    driver.get(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")

    for _ in range(100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    tags = driver.find_elements(By.CLASS_NAME, "tag-row")
    o_tags = []

    for tag in tags:
        tag_text = tag.text
        if 'Annotation' not in tag_text:
            o_tags.append(tag.text)

    for tag in o_tags:
        print(tag)

print("Search Magic: The Gathering card")
query = input('> ')
print(f"Obtaining Oracle Tags for {query}...")

card = scrython.cards.Named(fuzzy=query)
set_code = card.set_code()
collector_number = card.collector_number()

find_tags(set_code, collector_number)