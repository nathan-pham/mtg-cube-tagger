import scrython
import csv
from urllib.request import urlopen
import json

class Card:
    def __init__(self, name):
        self.scryfall = scrython.cards.Named(exact=name)
        self.name = self.scryfall.name()
        self.oracleID = self.scryfall.oracle_id()
        self.tags = []

class cardList:
    def __init__(self, csvPath, mode):
        cardList.csvPath = csvPath
        cardList.csvFile = []
        cardList.fieldnames = []

        cardList.oracleTags = []
        cardList.illustrationTags = []
        cardList.load_tags(self)

        cardList.allTags = []
        cardList.cards = cardList.import_cards(self)

        cardList.write_tags(self)
        cardList.write_stats(self)
    
    def import_cards(self):
        cards = []
        with open(self.csvPath, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            cardList.fieldnames = reader.fieldnames

            for row in reader:
                newCard = Card(row['name'])
                print(f"Searching tags for {newCard.name}...")
                newCard.tags = self.find_tags(newCard.oracleID)

                for tag in newCard.tags:
                    if tag not in cardList.allTags:
                        cardList.allTags.append(tag)

                cards.append(newCard)
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

    def write_stats(self):
        """
        A function that writes all the unique tags read into a txt file
        """
        with open('tags.txt', mode = 'x') as tagsfile:
            for tag in self.allTags:
                tagsfile.write(f"{tag}\n")
        tagsfile.close()
        
    def load_tags(self):
        print("Opening tag database...")

        urlOracle = (f'https://api.scryfall.com/private/tags/oracle')
        responseOracle = urlopen(urlOracle)

        urlIllustration = (f'https://api.scryfall.com/private/tags/illustration')
        responseIllustration = urlopen(urlIllustration)        
        
        if mode == 'all':
            self.oracleTags = json.loads(responseOracle.read())
            self.illustrationTagsTags = json.loads(responseIllustration.read())
            
        elif mode == 'oracle':
            self.oracleTags = json.loads(responseOracle.read())

        elif mode == 'illustration':
            self.illustrationTagsTags = json.loads(responseIllustration.read())

        print("Tag database initialised!")

    def find_tags(self, oracleID):
            oracle_tags = []

            if self.oracleTags:
                for tag in self.oracleTags['data']:
                    if oracleID in tag['oracle_ids']:
                        oracle_tags.append(tag['label'].strip('"'))

            if self.illustrationTags:
                for tag in self.illustrationTags['data']:
                    if oracleID in tag['oracle_ids']:
                        oracle_tags.append(tag['label'].strip('"'))   

            return oracle_tags

if __name__ == "__main__":
    
    print("Which tags do you want to load? (oracle/illustration/all)")
    mode = input("> ")

    print("What's the name of your cube? (eg. mycube.csv)")
    cubeName = input("> ")

    cardList(f"card_lists/{cubeName}", mode)