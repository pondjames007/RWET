import random
import tracery
from tracery.modifiers import base_english
import json
import pyphen
import subprocess
import makegif
from selenium import webdriver

dic = pyphen.Pyphen(lang='nl_NL')

adverbs_data = json.load(open("adverbs.json", "r"))
adverbs = [item for item in adverbs_data["adverbs"] if len(dic.inserted(item).split("-")) == 1]
# print("ADV:")
# print(adverbs)

verbs = []
verbs_two = []
verbs_data = json.load(open("verbs.json", "r"))
for item in verbs_data["verbs"]:
    if len(dic.inserted(item["present"]).split("-")) == 1:
        verbs.append(item["present"])
    elif len(dic.inserted(item["present"]).split("-")) == 2:
        verbs_two.append(item["present"])
# print("VERBS")
# print(verbs)
# print(verbs_two)


nouns_data = json.load(open("nouns.json", "r"))
nouns = [item for item in nouns_data["nouns"] if len(dic.inserted(item).split("-")) == 1]
nouns_two = [item for item in nouns_data["nouns"] if len(dic.inserted(item).split("-")) == 2]
# print("NOUNS")
# print(nouns)
# print(nouns_two)

description_data = json.load(open("descriptions.json", "r"))
descriptions = [item for item in description_data["descriptions"] if len(dic.inserted(item).split("-")) == 1]
descriptions_two = [item for item in description_data["descriptions"] if len(dic.inserted(item).split("-")) == 2]
# print(descriptions)
# print(descriptions_two)

moods_data = json.load(open("moods.json", "r"))
moods = [item for item in moods_data["moods"] if len(dic.inserted(item).split("-")) == 1]
moods_two = [item for item in moods_data["moods"] if len(dic.inserted(item).split("-")) == 2]
# print(moods)
# print(moods_two)

rules = {
    "sentence_a":["#adj.capitalize# #noun# #adv# #verb#, #noun# #verb# #adv#, #adv# #adj# #adv# #adj# #noun_two#"],
    "sentence_b":["#adj.capitalize# #noun# #adv# #verb#, #noun# #verb# #adv#, #noun_two# #noun_two# #noun_two#"],
    "sentence_c":["#adj.capitalize# #noun# #adj# #noun#, #adj# #noun# #adj# #noun#, #verb_two# #adj_two# #noun_two#"],
    "sentence_d":["#noun_two.capitalize# #verb# #noun#, #adj_two# #adj_two# #noun_two#"],
    "sentence_e":["#adv.capitalize# #verb# #noun_two# #adj# #noun#, #noun_two# #adv# #verb_two#, #adj# #noun# #adv# #verb#"],
    "sentence_f":["#adj.capitalize# #noun# #adj# #noun#, #verb# and #verb#, #adj# #noun# #adv# #verb# #adv# #verb#"],
    "sentence_g":["#adj.capitalize# #noun# #adv# #verb#, #adj# #noun# should #verb# #noun#, #adv# #verb# #adj# #noun#"],
    "sentence_h":["#noun_two.capitalize# #verb# #noun#, #adj_two# just #verb# #noun_two#"],
    "noun":nouns,
    "noun_two":nouns_two,
    "verb":verbs,
    "verb_two":verbs_two,
    "adj":["#descriptions#", "#moods#"],
    "adj_two":["#descriptions_two#", "#moods_two#"],
    "adv":adverbs,
    "descriptions":descriptions,
    "descriptions_two":descriptions_two,
    "moods":moods,
    "moods_two":moods_two
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

poem = []
poemStr = ""
count = 0

for key in rules:
    if count < 8:
        poem.append(grammar.flatten("#"+key+"#"))
        poemStr += grammar.flatten("#"+key+"#") + "\n"
    else:
        break
    count += 1

print(poem)
with open("poem.txt", 'w') as infile:
    infile.write(poemStr)

sentences = []
for item in poem:
    sentences.extend(item.split(","))

img_cnt = 0
for sentence in sentences:
    finished = False
    words = sentence.strip().split(" ")
    bound = 0
    count = len(words)
    # print(count)
    
    while finished == False:
        queryStr = " ".join(words[bound:count])
        result = makegif.get_images(queryStr, img_cnt)
        if result == False:
            count -= 1
        else:
            img_cnt += 1
            if count == len(words):
                finished = True
            else:
                bound = count
                count = len(words)

subprocess.call(["convert","-delay", "200", "frames/*.jpg", "output.gif"])
driver = webdriver.Chrome()
driver.get("file:///Users/pondjames007/Desktop/ITP_Classes/RWET/finalProject/output.gif")