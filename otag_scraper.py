import scrython
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
import csv

# Set up ChromeDriver settings
chromedriver_path = '/usr/bin/chromedriver'
service = Service(chromedriver_path)
options = ChromiumOptions()
options.add_argument("--headless=new")
options.add_argument('--blink-settings=imagesEnabled=false')

class Card:
    def __init__(self, name, mode):
        self.scryfall = scrython.cards.Named(fuzzy=name)
        self.name = self.scryfall.name()
        self.link = self.find_link()
        self.tags = self.find_tags(self.link, mode)
        self.mode = mode

    def find_tags(self, link, mode):

        # Initialise driver
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(link)

        # Scroll down page
        for _ in range(50):
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
            o_tags.append(tag.text)

        driver.quit()

        # Verbose debuggging
        print(self.name)
        print(o_tags)

        return o_tags

    def find_link(self):
        set_code = self.scryfall.set_code()
        collector_number = self.scryfall.collector_number()
        return(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")

class cardList:
    def __init__(self, csvPath):
        cardList.csvPath = csvPath
        cardList.cards = cardList.import_cards(self)
        cardList.namePos = int
        cardList.tagsPos = int
    
    def import_cards(self):

        cards = []

        with open(self.csvPath, newline='') as csvfile:
            reader = csv.reader(csvfile)

            # Find which columns are the name and tag columns
            firstRow = next(reader)
            for i in range(len(firstRow)):
                if (firstRow)[i] == 'name':
                    self.namePos = i
                elif (firstRow)[i] == 'tags':
                    self.tagsPos = i

            for i in reader:
                print("Loading...")
                cards.append(Card(i[self.namePos], "all"))
    
        return cards
    
    def write_tags(self):
        with open(self.csvPath, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, 'tags')
            next(writer)

            for i in range(1, len(writer)):
                writer.writerow({'tags': cardList.cards[i].tags})
                i += 1

            writer.close()


if __name__ == "__main__":
    cardList('example.csv')
    for i in cardList.cards:
        print(i.tags)