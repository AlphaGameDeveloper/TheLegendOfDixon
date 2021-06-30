#Import modules
import random
import time
import json
import subprocess
import math
import os
import platform
import sys
import pathlib
#_________________________
global randomSeed
randomSeed=random.randint(100000000,999999999)
#Make functions
def typeEffect(text):
    for i in text:
        sys.stdout.write(i)
        time.sleep(.1)
def save():
    with open('assets/save/saveGame.json', 'w') as savePath:
        json.dump(saveFile, savePath)
        return(True)
def pause():
    input('press ENTER to continue')
def clear():
    for i in range(50):
        print()
def getMenuChoice(minimum, maximum):
    try:
        f=int(input('> '))
        if(f >= minimum and f <= maximum):
            return(f)
        else:
            print('Number out of range!!')
            print('Your number should be between '+str(minimum)+' and '+str(maximum)+'.')
            pause()
            return(getMenuChoice(minimum, maximum))
    except:
        print('YOU DID NO ENTER A NUMBER!')
        print('ENTER A NUMBER NEXT TIME!')
        pause()
        return(getMenuChoice(minimum, maximum))
def fight(opponent):
    opponentData={ #Make a copy so the opiginal data is not affected.
        "name": opponent['name'],
	    "HP": opponent['HP'],
	    "attk": opponent['attk'],
	    "inte": opponent['inte'],
	    "def": opponent['def']
    }
    print('You are in a fight with a '+opponentData['name']+'!  Here are your options:')
    print('1 - Fight back\n2 - Play dead\n3 - ')
#__________________________
clear()
print('loading...')
time.sleep(1)
fileParentDir=pathlib.Path(__file__).parent.absolute()
os.chdir(fileParentDir)
print('Getting save file... please wait...')
with open('assets/save/saveGame.json') as file:
    print('searching in assets/save/saveGame.json')
    global saveFile
    saveFile=json.load(file)
    print('got data for SaveFile:')
    print(saveFile)
print()
print('getting JSON data for creeper...')
with open('assets/monsters/creeper.json') as path:
    print('searching in assets/monsters/creeper.json')
    global creeperData
    creeperData=json.load(path)
    print('got data for creeper:')
    print(creeperData)
time.sleep(.1)
print()
print('getting JSON data for skeleton')
with open('assets/monsters/skeleton.json') as path:
    print('searching in assets/monsters/skeleton.json')
    global skeletonData
    skeletonData=json.load(path)
    print('got data for skeleton:')
    print(skeletonData)
time.sleep(.1)
print()
print('getting JSON data for zombie')
with open('assets/monsters/zombie.json') as path:
    print('searching in assets/monsters/zombie.json')
    global zombieData
    zombieData=json.load(path)
    print('got data for zombie:')
    print(zombieData)
time.sleep(.1)
print()
print('done getting JSON data for monsters; getting JSON data for items')
print()
print('getting JSON data for default_sword')
with open('assets/items/default_sword.json') as path:
    print('searching in assets/items/default_sword.json')
    global defaultSwordData
    defaultSwordData=json.load(path)
    print('got data for default_sword:')
    print(defaultSwordData)
time.sleep(.1)
print()
print('getting JSON data for master_sword')
with open('assets/items/master_sword.json') as path:
    print('searching in assets/items/master_sword.json')
    global masterSwordData
    masterSwordData=json.load(path)
    print('got data for master_sword:')
    print(masterSwordData)
print()
clear()
def mainMenu():
    print('The Legend Of Dixon:')
    print('Why Am I Making This?')
    print('\nA program by Damien B.')
    if(saveFile['isNewSave']==True):
        print('\n\n1 - Continue')
    else:
        print('\n\n1 - Continue Save Game (level '+saveFile['lvl']+')')
    print('2 - Start New Save (ALL data will be erased and not retrevable!)')
    print('3 - Credits')
    print('4 - Quit')
    g=getMenuChoice(1,4)
    if(g==1):
        saveFile['isNewSave']=False
        saveFile['lvl']=1
        saveFile['saveName']=input('Enter the save name: ')
        save()
    if(g==2):
        saveFile['isNewSave']=True
        saveFile['lvl']=0
        saveFile['saveName']=None
        print('SaveFile wiped sucessfully.')
        clear()
        mainMenu()
mainMenu()