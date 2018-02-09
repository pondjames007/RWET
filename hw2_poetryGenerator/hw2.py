import random
import textwrap

newspaper = []
newspaper.append("""Nintendo Labo's cardboard accessories can interact with the Switch in a number of ways.
For example, by popping out pre-cut pieces, users can build a piano that plays musical notes or an RC
car that can be controlled with the gaming console. The kits are aimed at children ages 6 to 12 and
go on sale starting April 20. The variety kit -- which includes projects like a fishing rod and piano
-- will cost $70, while the robot kit sells for $80. The Nintendo Switch ($300) is sold separately.
At a recent event in New York City, CNN Tech got an early look at the new low-tech creations, which
Nintendo calls "Toy-Cons." """)

newspaper.append("""The billionaire CEO of SpaceX hosted a press conference after the company's
Falcon Heavy rocket aced its first launch Tuesday. The new rocket is slated to fly a hefty
telecommunications satellite for Arabsat, a Saudi Arabia-based firm, during the first half of 2018.
It's also signed up to deliver a payload for the U.S. Air Force sometime this year.
But Musk was more interested in talking about what SpaceX will build next.
And he made it clear the company is still focused on its ultimate goal: Sending humans to live on Mars.""")

newspaper.append("""a nonprofit that sets the global standard for emoji -- announced on Wednesday 157 new emoji
options would be coming later this year. The latest collection includes a cupcake, lobster, pirate flag and
more expressive smiley faces. Emoji will soon have a variety of new hairstyles, such as curly or bald, and
more hair color options such as red and white. There will also be more animals, such as a kangaroo, llama,
swan and mosquito. More fun smiley faces include a "cold face" with dangling icicles, a partying face and a "woozy" emoji.""")

words = []
for news in newspaper:
    words += news.split()
    random.shuffle(words)

title = []
output = []
for i in range(100):
    if i < 10:
        title.append(random.choice(words))
    output.append(words[i])

print("\""," ".join(title).title(), "\"\n")
print(textwrap.fill(" ".join(output), 60))
