# Scryfall Oracle-Tag Web Scraper
## Background
As someone interested in Magic: The Gathering cube design, being able to categorise my cards by their function in the game is extremely useful, but there isn't a way to do so automatically using CubeCobra, nor is there a way to get the Oracle Tags of a card from Scryfall's Bulk Data as of yet. 

Since going through the tagger pages for hundreds of cards and manually adding them to my cube on CubeCobra would be an arduous task, I decide to build this program.

## Function
Given an exported CSV file from a CubeCobra cube, this program searches every card on tagger.scryfall.com and web-scrapes its tags (artwork, card function or both) and writes them to the 'tag' field in the CSV. The now updated CSV can be uploaded back into CubeCobra with all the cards having their tags.

## Dependencies
- This program was programmed/tested on Python 3.12.3
- Selenium
- [Scrython](https://github.com/NandaScott/Scrython/tree/main)
    - asyncio
    - aiohttp

## Usage
1. Export your cube from CubeCobra as a CSV (this program has only been tested with the 'Use Sort' and 'Use Filter' options turned off during exporting)
2. Place your cube into the card_lists folder and rename it to cardlist.csv
3. By default, the program is set to only search for the card function tags. To change this, you must edit line 83 of otag_scraper.py and change the "card" argument to either "all", "art" or "card".
4. Save the program and run.
5. After its completion your CSV file should be updated with all the tags.

## Notes
According to a ticket I submitted with Scryfall support, oracle tags will be added to the bulk data export in Scryfall in the future (time unspecified), so hopefully eventually there will be no need for this repo!

Thanks to the teams at Scryfall, CubeCobra and Scrython for all the hard work they've put in making these wonderful services for nerds like us.

**Warning:** Due to the nature of web scraping, use this tool responsibly as to not abuse Scryfall servers/API calls in line with their TOS.

### Runtime test history
Start 12:09 PM, Finish 12:11 PM (Scrython error)

Start 12:17 PM, Finish 12:35 PM finished scraping portion (some tags missing)

Start 11:52AM, Finish 12:00 failiure

Start 12:00, Finish 12:03 failiure

Start 12:03, Finish 12:19 success (both tag scraping and CSV writing) = 16 minutes for 360 cards