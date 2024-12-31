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
        self.scryfall = scrython.cards.Named(exact=name)
        self.name = self.scryfall.name()
        self.link = self.find_link()
        self.tags = self.find_tags(self.link, mode)
        self.mode = mode

    def find_tags(self, link, mode):

        # Initialise driver
        driver = webdriver.Chrome(options=options, service=service)
        driver.get(link)

        o_tags = []
        while not o_tags:

            print(f"Searching {self.name}...")

            # Scroll down page
            for _ in range(100):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Find elements based on mode selected
            if mode == 'all':
                tags = driver.find_elements(By.XPATH, "//a[contains(@href, '/tags/')]")
            elif mode == 'art':
                tags = driver.find_elements(By.XPATH, "//a[contains(@href, '/tags/artwork/')]")
            elif mode == 'card':
                tags = driver.find_elements(By.XPATH, "//a[contains(@href, '/tags/card/')]")

            # Convert tags to strings and append to new list
            for tag in tags:
                o_tags.append(tag.text.strip('"'))

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
        cardList.csvFile = []
        cardList.cards = cardList.import_cards(self)
        cardList.write_tags(self)
        cardList.fieldnames = []
    
    def import_cards(self):
        cards = []
        with open(self.csvPath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            cardList.fieldnames = reader.fieldnames

            for row in reader:
                print("Loading...")
                cards.append(Card(row['name'], "all"))
                cardList.csvFile.append(row)
    
        csvfile.close()
        return cards
    
    def write_tags(self):

        for i in range(len(self.csvFile)):
            tags = ";".join(self.cards[i].tags)
            self.csvFile[i]['tags'] = tags

        with open(self.csvPath, mode='w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()
        
            writer.writerows(self.csvFile)
        
    def print_cards(self):
        """
        Debugging function
        """
        with open(self.csvPath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print(reader)
        
            for row in reader:
                print(row)
        

if __name__ == "__main__":
    cardList('card_lists/short_cardlist.csv')