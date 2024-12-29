import scrython
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions


# Set up ChromeDriver settings
chromedriver_path = '/usr/bin/chromedriver'
service = Service(chromedriver_path)
options = ChromiumOptions()
options.add_argument("--headless=new")


def find_tags(set_code, collector_number):
    print(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")

    # Initialise driver
    driver = webdriver.Chrome(options=options, service=service)
    driver.get(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")

    # Scroll down page
    for _ in range(100):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Find all elements with class "tag-row"
    tags = driver.find_elements(By.CLASS_NAME, "tag-row")

    # Convert tags to strings and append to new list
    o_tags = []
    for tag in tags:
        tag_text = tag.text
        if 'Annotation' not in tag_text:
            o_tags.append(tag.text)

    for tag in o_tags:
        print(tag)

    driver.quit()

print("Search Magic: The Gathering card")
query = input('> ')
print(f"Obtaining Oracle Tags for {query}...")

card = scrython.cards.Named(fuzzy=query)
set_code = card.set_code()
collector_number = card.collector_number()

find_tags(set_code, collector_number)