#!/usr/bin/python

import os, sys
from PIL import Image

print(""" _____  ____  __  __   _______         __  __ _      
|  __ \|  _ \|  \/  | |__   __|       / _|/ _(_)     
| |  | | |_) | \  / |    | |_ __ __ _| |_| |_ _  ___ 
| |  | |  _ <| |\/| |    | | '__/ _` |  _|  _| |/ __|
| |__| | |_) | |  | |    | | | | (_| | | | | | | (__ 
|_____/|____/|_|  |_|    |_|_|  \__,_|_| |_| |_|\___|""")

def process(filename):
  def centercrop(image):
    width, height = image.size

    
    
    left = 0
    top = 0
    right = width
    bottom = height - number

    img = image.crop((left, top, right, bottom))
    return img
  try:
    im = Image.open(filename)
    im = centercrop(im)
    im.save(filename)
    print("cropped", filename)
  except IOError:
    pass
number = int(input("Podaj ile pixeli skrocic od dolu: "))
path = input("Podaj sciezke do folderu: ")
dirs = os.listdir(path)

for file in dirs:
  process(path + "/" + file)

