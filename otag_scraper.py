import scrython
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
import csv
from urllib.request import urlopen
import json

class Card:
    def __init__(self, name, mode):
        self.scryfall = scrython.cards.Named(exact=name)
        self.name = self.scryfall.name()
        self.oracleID = self.scryfall.oracle_id()
        self.tags = self.find_tags()
        self.mode = mode

    def find_tags(self):
        oracle_tags = []

        for tag in data_json['data']:
            if self.oracleID in tag['oracle_ids']:
                oracle_tags.append(tag['label'].strip('"'))

        return oracle_tags

class cardList:
    def __init__(self, csvPath):
        cardList.csvPath = csvPath
        cardList.csvFile = []
        cardList.fieldnames = []
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
                newCard = Card(row['name'], "card")
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
    cardList('card_lists/cardlist.csv')