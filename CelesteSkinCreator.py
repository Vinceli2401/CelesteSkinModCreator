import os
import sys
import shutil
from distutils.dir_util import copy_tree
import glob
from PIL import Image
import numpy as np
#install all the libraries before using the program!!!

skinName = input("Please input your skin name:")
authorName = input("Please input the author name:")
dash0 = "FFAABB" #hair color for the dashes, alter at own use, hexadecimal color code
dash1 = "EE7788"
dash2 = "BB5577"

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
                img.putpixel((i,j),(255, 170, 187)) #rgb color code for color you want to change
            if (data[0]==63 and data[1]==63 and data[2]==116): #sleeves
                img.putpixel((i,j),(255, 136, 153))
            if (data[0] == 69 and data[1] == 40 and data[2] == 60): #collar
                img.putpixel((i, j), (136, 68, 85))
            if (data[0] == 135 and data[1] == 55 and data[2] == 36): #trousers
                img.putpixel((i, j), (187, 85, 119))
    img.save(image)