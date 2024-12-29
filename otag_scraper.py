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


class Card:
    def __init__(self, name):
        self.name = name
        self.link = self.find_link(self.name)
        self.tags = self.find_tags(self.link)

    def find_tags(link):

        print("Which tags would you like to search for? (all/art/card)")
        mode = input('> ')

        # Initialise driver
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(link)

        # Scroll down page
        for _ in range(100):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Find elements based on mode selected
        # 'all' = all tags
        # 'art' = artwork tags only
        # 'card' = card tags only
        if mode == 'all':
            tags = driver.find_elements(By.XPATH, "//a[contains(@href, '/tags/')]")
        elif mode == 'art':
            tags = driver.find_elements(By.XPATH, "//a[contains(@href, '/tags/artwork/')]")
        elif mode == 'card':
            tags = driver.find_elements(By.XPATH, "//a[contains(@href, '/tags/card/')]")

        # Convert tags to strings and append to new list
        o_tags = []
        for tag in tags:
            tag_text = tag.text
            o_tags.append(tag.text)

        for tag in o_tags:
            print(tag)

        driver.quit()

        return o_tags

    def find_link(name):
        card = scrython.cards.Named(fuzzy=query)
        set_code = card.set_code()
        collector_number = card.collector_number()
        return(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")
