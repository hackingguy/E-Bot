#!/usr/bin/env python3
import sys
import os

choice=-1
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END,TICK = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\u2713'

# display heading
def heading():
    spaces = " " * 76
    print('\033c')
    sys.stdout.write(GREEN + spaces + """
           ▄████████      ▀█████████▄   ▄██████▄      ███
          ███    ███        ███    ███ ███    ███ ▀█████████▄
          ███    █▀         ███    ███ ███    ███    ▀███▀▀██
         ▄███▄▄▄           ▄███▄▄▄██▀  ███    ███     ███   ▀
        ▀▀███▀▀▀          ▀▀███▀▀▀██▄  ███    ███     ███
          ███    █▄         ███    ██▄ ███    ███     ███
          ███    ███        ███    ███ ███    ███     ███
          ██████████      ▄█████████▀   ▀██████▀     ▄████▀
    """.center(98) + END + BLUE +
    '\n' + '{}Download Entertainment Stuff ({}Entertainment Bot{}){}'.format(YELLOW, RED, YELLOW, BLUE).center(90) +
    '\n' + 'Made With <3 by: {0}Hacking Guy'.format(YELLOW).center(75) +
    '\n' + 'Version: {}1.0{} \n'.format(YELLOW, END).center(75))

try:
    while(True):

        heading()
        print("\n{}1.{}Anime Bot\n{}2.{}Hollywood Bot\n{}3{}.Bollywood Bot\n{}4.{}Exit\n\n{}Select Any Bot:{}".format(GREEN,WHITE,GREEN,WHITE,GREEN,WHITE,GREEN,WHITE,GREEN,WHITE),end="")


        choice = int(input())
        dir_path = os.path.dirname(os.path.realpath(__file__))
        if(choice==1):
            os.system("{}/anime.py".format(dir_path))
            input()
        elif(choice==2):
            os.system("{}/bollywood.py".format(dir_path))
        elif(choice==3):
            os.system("{}/hollywood.py".format(dir_path))
        elif(choice==4):
            break
        heading()
    
    print("\n{}Thanks For Visiting Us!".format(YELLOW))

except Exception as e:
    heading()
    print("\n{}Thanks For Visiting Us!\n{}".format(YELLOW,e))
