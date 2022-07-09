import os
import sys
import shutil
from distutils.dir_util import copy_tree
import glob
from PIL import Image
from PIL import ImageColor
import numpy as np
#install all the libraries before using the program!!!

skinName = input("Please input your skin name:")
authorName = input("Please input the author name:")
dash0 = input("Please input the hair color for zero dash:") #hair color for the dashes, alter at own use, hexadecimal color code
dash1 = input("Please input the hair color for one dash:")
dash2 = input("Please input the hair color for two dash:")

shirt = input('Input hex color for shirt: ')
shirt = ImageColor.getrgb('#' + shirt)
sleeves = input('Input hex color for sleeves: ')
sleeves = ImageColor.getrgb('#' + sleeves)
collar = input('Input hex color for collar: ')
collar = ImageColor.getrgb('#' + collar)
trousers = input('Input hex color for trousers: ')
trousers = ImageColor.getrgb('#' + trousers)

from_directory = "./SkinBase"
to_directory = skinName
copy_tree(from_directory, to_directory)

with open('./'+skinName+'/everest.yaml', encoding='UTF-8', mode='r') as file:
    newlines = []
    for line in file:
        newlines.append(line.replace('Replace', skinName))

with open('./'+skinName+'/everest.yaml', encoding='UTF-8', mode='w') as file:
    for line in newlines:
        file.write(line)

with open('./'+skinName+'/SkinModHelperConfig.yaml', encoding='UTF-8', mode='r') as file:
    newlines = []
    for line in file:
        newlines.append(line.replace('Author_Skin', authorName +"_"+ skinName).replace("Dash0",dash0).replace("Dash1",dash1).replace("Dash2",dash2))

with open('./'+skinName+'/SkinModHelperConfig.yaml', encoding='UTF-8', mode='w') as file:
    for line in newlines:
        file.write(line)

if not os.path.exists('./'+skinName+'/Graphics/' + authorName) :
    os.mkdir('./'+skinName+'/Graphics/' + authorName)
    os.mkdir('./'+skinName+'/Graphics/' + authorName + '/' + skinName)
os.replace('./'+skinName+'/Graphics/Author/Skin/Sprites.xml', './'+skinName+'/Graphics/' + authorName + '/' + skinName +'/Sprites.xml')
shutil.rmtree('./'+skinName+'/Graphics/Author')

with open('./'+skinName+'/Graphics/' + authorName + '/' + skinName +'/Sprites.xml', encoding='UTF-8', mode='r') as file:
    newlines = []
    for line in file:
        newlines.append(line.replace('Author/Skin', authorName +"/"+ skinName +'/characters'))

with open('./'+skinName+'/Graphics/' + authorName + '/' + skinName +'/Sprites.xml', encoding='UTF-8', mode='w') as file:
    for line in newlines:
        file.write(line)

with open('./'+skinName+'/Dialog/English.txt', encoding='UTF-8', mode='r') as file:
    newlines = []
    for line in file:
        newlines.append(line.replace('Author_Skin', authorName +"_"+ skinName).replace('skinName',skinName))

with open('./'+skinName+'/Dialog/English.txt', encoding='UTF-8', mode='w') as file:
    for line in newlines:
        file.write(line)

from_directory = './'+skinName+'/Graphics/Atlases/Gameplay/Author/Skin/characters'
to_directory = './'+skinName+'/Graphics/Atlases/Gameplay/'+authorName+'/'+skinName+'/characters'
copy_tree(from_directory, to_directory)
shutil.rmtree('./'+skinName+'/Graphics/Atlases/Gameplay/Author')

images=glob.glob('./'+skinName+'/Graphics/Atlases/Gameplay/'+authorName+'/'+skinName+'/characters/**/*.png')



for image in images:
    img = Image.open(image)
    width = img.size[0]
    height = img.size[1]
    for i in range(0,width):
        for j in range(0,height):
            data = img.getpixel((i,j))
            if (data[0]==91 and data[1]==110 and data[2]==225): #shirt
                img.putpixel((i,j),shirt) #rgb color code for color you want to change
            if (data[0]==63 and data[1]==63 and data[2]==116): #sleeves
                img.putpixel((i,j),sleeves)
            if (data[0] == 69 and data[1] == 40 and data[2] == 60): #collar
                img.putpixel((i, j),collar)
            if (data[0] == 135 and data[1] == 55 and data[2] == 36): #trousers
                img.putpixel((i, j),trousers)
    img.save(image)