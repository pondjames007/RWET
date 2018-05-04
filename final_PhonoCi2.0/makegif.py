import requests
from bs4 import BeautifulSoup
import os
import sys
import random
from PIL import Image, ImageDraw, ImageFont
import textwrap

def download_file(url, local_filename=None):

    if local_filename is None:
        local_filename = url.split('/')[-1]

    # if os.path.exists(local_filename):
        # return local_filename

    if not url.startswith('http'):
        url = 'http:' + url

    # NOTE the stram=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)

    return local_filename


def get_images(query, i):
    url = "https://www.shutterstock.com/search?searchterm=" + query
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    images = soup.select('.img-wrap > img')
    print(len(images))
    if len(images) == 0:
        return False
    else:
        img_url = random.choice(images).get("src")
        savedname = 'frames/' + str(i) + '.jpg'
        try:
            raw_image = download_file(img_url, savedname)
            print(raw_image)
            edit_image(raw_image, query)
            return True
        except Exception as e:
            print(e)
            return False


def edit_image(imagename, words):
    image = Image.open(imagename)
    image = image.resize((400,400))
    # print(image.size)
    canvas = ImageDraw.Draw(image, 'RGBA')
    useFont = "/Library/Fonts/Verdana.ttf"
    font = ImageFont.truetype(useFont, 30)

    # lines = textwrap.wrap(words, width=15)
    # y_height = 0
    # for line in lines:
    w, h = canvas.textsize(words, font=font)
    canvas.rectangle([0, (image.size[1]-h)/2, image.size[0], (image.size[1]+h)/2], fill=(0, 0, 0, 30))
    canvas.text(((image.size[0]-w)/2, (image.size[1]-h)/2) , words, font=font, fill=(255,255,255))
    # y_height += h
   
    out_image_name = imagename
    image.save(out_image_name)
    
# edit_image("frames/1.jpg", "lololololol")