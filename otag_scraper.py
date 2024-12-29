import scrython

card = scrython.cards.Named(fuzzy="Black Lotus")
set_code = card.set_code()
collector_number = card.collector_number()

print(f"https://tagger.scryfall.com/card/{set_code}/{collector_number}")