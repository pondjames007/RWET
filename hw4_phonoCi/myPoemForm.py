import tracery
from tracery.modifiers import base_english
import random
import json

venues_data = json.load(open("venues.json", "r"))
venues_one = []
venues_two = []

for venue_cat in venues_data["categories"]:
    for venue in venue_cat["categories"]:
        if len(venue["name"].split(" ")) == 1:
            venues_one.append(venue["name"].lower())
        elif len(venue["name"].split(" ")) == 2:
            venues_two.append(venue["name"])

# print(venues)

character_data = json.load(open("character.json", "r"))
characters = []
qualities = []

for character in character_data["characters"]:
    characters.append(character["name"].lower())
    for quality in character["qualities"]:
        qualities.append(quality.lower())

# print(characters)
# print()
# print(qualities)


# print(regions)

rich_data = json.load(open("richpeople.json", "r"))
riches = []

for rich in rich_data["richPeople"]:
    if len(rich["name"].split(" ")) == 2:
        riches.append(rich["name"])

# print(riches)

mood_data = json.load(open("moods.json", "r"))
moods = mood_data["moods"]

# print(moods)

colors_data = json.load(open("crayola.json", "r"))
colors = []

for color in colors_data["colors"]:
    if len(color["color"].split(" ")) == 1:
        colors.append(color["color"].lower())

# print(colors)

menu_data = json.load(open("menuItems.json", "r"))
menus = [data.lower() for data in menu_data["menuItems"] if len(data.split(" "))==1]

# print(menus)

adverb_data = json.load(open("adverbs.json", "r"))
adverbs = adverb_data["adverbs"]

# print(adverbs)

verb_data = json.load(open("verbs.json", "r"))
verbs = []

for verb in verb_data["verbs"]:
    verbs.append(verb["past"])

# print(verbs)
# print("\n\n\n\n")
# venues_one, venues_two, characters, qualities, regions, riches, moods, color, menus

rules = {
    "sentence_a":["#adj.capitalize# #noun# #adv# #verb#, #noun# #verb# #adv#, #adv# #adj# #adv# #adj# #noun_two#"],
    "sentence_b":["#adj.capitalize# #noun# #adv# #verb#, #noun# #verb# #adv#, #noun# #noun# #noun_two# #noun_two#"],
    "sentence_c":["#adj.capitalize# #noun# #adj# #noun#, #adj# #noun# #adj# #noun#, #adv# #verb# #adj# #noun_two#"],
    "sentence_d":["#noun.capitalize# #noun# #verb# #noun#, #adv.a# #verb# #noun# #noun#"],
    "noun":["#venues#", "#characters#", "#menus#"],
    "noun_two":["#riches#", "#venues_two#"],
    "verb":verbs,
    "adj":["#qualities#", "#moods#", "#colors#"],
    "adv":adverbs,
    "venues":venues_one,
    "venues_two":venues_two,
    "characters":characters,
    "qualities":qualities,
    "riches":riches,
    "moods":moods,
    "colors":colors,
    "menus":menus
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
print(grammar.flatten("#sentence_a#"))
print(grammar.flatten("#sentence_b#"))
print(grammar.flatten("#sentence_c#"))
print(grammar.flatten("#sentence_d#"))

# print()
# print(base_english)

# 4-3-6  adj-n-adv-v, n-v-adv, adv-adj-adv-adj-n-n
# 4-3-6  
# 4-4-5  adj-n-adj-n, adj-n-adj-n, adv-v-adj-n-n
# 4-6    n-n-v-n, a/an adv-v-n-n