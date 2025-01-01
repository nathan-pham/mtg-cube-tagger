# Scryfall Oracle-Tag Web Scraper
## Background
As someone interested in Magic: The Gathering cube design, being able to categorise my cards by their function in the game is extremely useful, but there isn't a way to do so automatically using CubeCobra, so I wrote a script to automatically add Scryfall tagger data to a CubeCobra cube.

## Usage
1. Export your cube from CubeCobra in CSV format
2. Run the mtg-cube-tagger.py program (after installing dependencies)
3. Follow prompts from program

## Dependencies
- This program was programmed/tested on Python 3.12.3
- [Scrython](https://github.com/NandaScott/Scrython/tree/main)
    - asyncio
    - aiohttp

## Known Issues
- The code has only been tested with CSV exported without 'Use Sort' and 'Use Filter' options, so with those enabled, I'm not sure how the code will function

## Usage
1. Export your cube from CubeCobra as a CSV (this program has only been tested with the 'Use Sort' and 'Use Filter' options turned off during exporting)
2. Place your cube into the card_lists folder and rename it to cardlist.csv
3. By default, the program is set to only search for the card function tags. To change this, you must edit line 83 of otag_scraper.py and change the "card" argument to either "all", "art" or "card".
4. Save the program and run.
5. After its completion your CSV file should be updated with all the tags.

## Acknowledgements
Thanks to the teams at Scryfall, CubeCobra and Scrython for all the hard work they've put in making these wonderful services for nerds like us.

Also a big thanks to [Jawn Snow](https://github.com/dsoskey) on the Cube Cobra Discord for pointing me towards the Scryfall API for tags, meaning I could write a program which is way quicker than the initial 1.0.0 version which used web scraping.