# Anime finder
# Created by Astral
# Date: 1/18/19

import time
import webbrowser

global anime_list
anime_list = ''

# Function to exec anime
def exec_anime(anime):
    webbrowser.open('https://www.crunchyroll.com/'+anime, new = 2)

def main_menu():
    menu = ['1','2', '3']
    print('1. Search for anime\n')
    print('2. Add anime to list\n')
    print('3. Load anime list')
    print(" ")

    menu_input = input('What would you like to do? \n')

    if menu_input == menu[0]:
        cls_screen()
        shows()

    elif menu_input == menu[1]:
        cls_screen()
        add_show()

    elif menu_input == menu[2]:
        cls_screen()
        load_show()

    else:
        error_handling()

def cls_screen():
    print("\n"*100)

def add_show():
    while True:
        user_data = input('What show would you like to add to your favorites? \n')
        with open ('data.txt','a') as f:
            f.write('\n' + user_data)
            f.close()
            print('Anime has successfully been added')
            time.sleep(3)
            
    else:
        print("Sorry the anime you wanted to add does not exist in the database")
               
def load_show():
   with open ('data.txt','r') as f:
       cls_screen()
       print(f.read())

def error_handling(message='Either the anime is not avalable or you entered it incorrectly, please try again'):
    cls_screen()
    print(message)
    time.sleep(3)
    

# A list of all animes that can be launched
def shows():
    anime_list = {
    'Attack on Titan': "attack-on-titan",
    'Bleach' : 'bleach',
    'Dragon Ball Super' : 'dragon-ball-super',
    'Black Clover': 'black-clover',
    'Sword Art Online': 'sword-art-online',
    'GOBLIN SLAYER': 'goblin-slayer',
    'Fairy Tail': 'fairy-tail',
    'My Hero Academia': 'my-hero-academia',
    'Hunter x Hunter': 'hunter-x-hunter',
    'Rascal Does Not Dream of Bunny Girl Senpai': 'rascal-does-not-dream-of-bunny-girl-senpai',
    'KONOSUBA -God\'s blessing on this wonderful world!': 'konosuba-gods-blessing-on-this-wonderful-world',
    'Food Wars! Shokugeki no Soma': 'food-wars-shokugeki-no-soma',
    'ZOMBIE LAND SAGA': 'zombie-land-saga',
    'DARLING in the FRANXX': 'darling-in-the-franxx',
    'The Ancient Magus\' Bride': 'the-ancient-magus-bride',
    'Naruto': 'naruto',
    'Naruto Shippuden': 'naruto-shippuden',
    'PERSONA5 the Animation': 'persona5-the-animation',
    'Re:ZERO -Starting Life in Another World-': 'rezero-starting-life-in-another-world-',
    'Akame ga Kill!': 'akame-ga-kill',
    'Kuroko\'s Basketball': 'kurokos-basketball',
    'Parasyte -the maxim-': 'parasyte-the-maxim-',
    'MONSTER MUSUME EVERYDAY LIFE WITH MONSTER GIRLS': 'monster-musume-everyday-life-with-monster-girls',
    'Fullmetal Alchemist: Brotherhood': 'fullmetal-alchemist-brotherhood',
    'My First Girlfriend is a Gal': 'my-first-girlfriend-is-a-gal',
    'Berserk': 'berserk',
    'Your lie in April': 'your-lie-in-april',
    'Bakemonogatari': 'Bakemonogatari',
    'Keijo!!!!!!!!': 'keijo',
    'Another': 'another',
    'Kill la Kill': 'kill-la-kill',
    'Fist of the North Star': 'fist-of-the-north-star',
    'Yamada-kun and the Seven Witches': 'yamada-kun-and-the-seven-witches',
    'Love, Chunibyo & Other Delusions': 'love-chunibyo-other-delusions-heart-throb-',
    'Arpeggio of Blue Steel': 'arpeggio-of-blue-steel',
    'GIRLS und PANZER': 'girls-und-panzer'
    }

# Statments to compare user input to the dict, if matches launch anime
    while True:
        cls_screen()
        userInput = input('What anime would you like to watch?\n')
        if userInput in anime_list:
                exec_anime(anime_list[userInput])
                break
        else:
                error_handling()
  

def main():
    main_menu()

main()