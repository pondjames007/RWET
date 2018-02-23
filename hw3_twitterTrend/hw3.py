import random

trends = []
trends.append([line.strip() for line in open("twitter_trend_US.txt", "r")])
trends.append([line.strip() for line in open("twitter_trend_US2.txt", "r")])
trends.append([line.strip() for line in open("twitter_trend_UK.txt", "r")])
trends.append([line.strip() for line in open("twitter_trend_UK2.txt", "r")])
trends.append([line.strip() for line in open("twitter_trend_SG.txt", "r")])
trends.append([line.strip() for line in open("twitter_trend_SG2.txt", "r")])
trends.append([line.strip() for line in open("twitter_trend_WORLD.txt", "r")])
trends.append([line.strip() for line in open("twitter_trend_WORLD2.txt", "r")])


my_tags_all = []
my_tags_us = []
my_tags_uk = []
my_tags_sg = []
my_tags_wd = []

for i in range(10):
    tag_all = ""
    tag_us = ""
    tag_uk = ""
    tag_sg = ""
    tag_wd = ""
    for j in range(4):
        tag_all += random.choice(trends[random.randint(0, 7)])
        tag_us += random.choice(trends[random.randint(0, 1)])
        tag_uk += random.choice(trends[random.randint(2, 3)])
        tag_sg += random.choice(trends[random.randint(4, 5)])
        tag_wd += random.choice(trends[random.randint(6, 7)])

    tag_all = tag_all.replace(" ", "")
    tag_us = tag_us.replace(" ", "")
    tag_uk = tag_uk.replace(" ", "")
    tag_sg = tag_sg.replace(" ", "")
    tag_wd = tag_wd.replace(" ", "")
    # tag_all = tag_all.strip()
    # tag_us = tag_us.strip()
    # tag_uk = tag_uk.strip()
    # tag_sg = tag_sg.strip()
    # tag_wd = tag_wd.strip()

    if tag_all[0] != "#":
        tag_all = "#" + tag_all
    if tag_us[0] != "#":
        tag_us = "#" + tag_us
    if tag_uk[0] != "#":
        tag_uk = "#" + tag_uk
    if tag_sg[0] != "#":
        tag_sg = "#" + tag_sg
    if tag_wd[0] != "#":
        tag_wd = "#" + tag_wd

    my_tags_all.append(tag_all)
    my_tags_us.append(tag_us)
    my_tags_uk.append(tag_uk)
    my_tags_sg.append(tag_sg)
    my_tags_wd.append(tag_wd)

print("My Tags Trend - All")
for tag in my_tags_all:
    print(tag)
print()
print("My Tags Trend - US")
for tag in my_tags_us:
    print(tag)
print()
print("My Tags Trend - UK")
for tag in my_tags_uk:
    print(tag)
print()
print("My Tags Trend - SG")
for tag in my_tags_sg:
    print(tag)
print()
print("My Tags Trend - WORLD")
for tag in my_tags_wd:
    print(tag)
print()
