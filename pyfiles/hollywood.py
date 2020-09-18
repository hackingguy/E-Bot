#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# HollyBot.py
try:
    import os
    import sys
    import html
    import requests
    from bs4 import BeautifulSoup as soup
except Exception as e:
    print(e)
    exit()

#Debug
DEBUG=False

#Websites Don't Allow To Enter If You Don't Use Good Headers
#I Love Apple Headers (Macintosh), Even I don't have one till now :)>
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#My Favourite Shell GUI
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END,TICK = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\u2713'


# display heading
def heading():
    spaces = " " * 76
    print('\033c')
    sys.stdout.write(GREEN + spaces + """
                • ▌ ▄ ·.        ▌ ▐·▪  ▄▄▄ ..▄▄ ·     ▄▄▄▄·       ▄▄▄▄▄
                ·██ ▐███▪▪     ▪█·█▌██ ▀▄.▀·▐█ ▀.     ▐█ ▀█▪▪     •██  
                ▐█ ▌▐▌▐█· ▄█▀▄ ▐█▐█•▐█·▐▀▀▪▄▄▀▀▀█▄    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
                ██ ██▌▐█▌▐█▌.▐▌ ███ ▐█▌▐█▄▄▌▐█▄▪▐█    ██▄▪▐█▐█▌.▐▌ ▐█▌·
                ▀▀  █▪▀▀▀ ▀█▄▀▪. ▀  ▀▀▀ ▀▀▀  ▀▀▀▀     ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 

    """.center(98) + END + BLUE +
    '\n' + '{}Download Any Movie You Want ({}Movie Bot{}){}'.format(YELLOW, RED, YELLOW, BLUE).center(102) +
    '\n' + 'Made With <3 by: {0}Hacking Guy'.format(YELLOW).center(86) +
    '\n' + 'Version: {}1.0{} \n'.format(YELLOW, END).center(86))

#Error Handling
def errorOccured(fun_name,e):
    if(DEBUG==False):
            print("{}May Be There Is Problem\nCheck Internet Connection Or Report Us Issue at https://github.com/hackingguy/E-Bot/Issues".format(RED))
            exit()
    else:
            print("Exception Occured:\nFunction:{}\n{}".format(fun_name,e))

def search(movie_name):
    myurl = "https://fmovies.top/?s="+movie_name
    req = requests.get(myurl, headers=headers)
    page_html = req.content
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"featuredItems singleVideo"})
    return containers

def getMovieURL(containers,choice):
    movie_url = "https://fmovies.top/movies/"+"-".join((containers[choice-1].a["oldtitle"]).split())+"/"
    req = requests.get(movie_url, headers=headers)
    page_html = req.content
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("a",{"class":"thumb mvi-cover"})
    movie_url = containers[0]["href"]
    return movie_url

def mainURL(movie_url):
    req = requests.get(movie_url, headers=headers)
    page_html = req.content
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("iframe",{"class":"metaframe rptss"})
    return containers[0]["src"]

try:
    heading()
    containers = search("+".join((input("\n{}Enter Movie Name:{}".format(GREEN,WHITE))).split()))
    numberOfMovies = len(containers)
    if(numberOfMovies==0):
      print("{}No Movies Found{}".format(RED,GREEN))
      input("{}Press Enter To Continue...{}".format(GREEN,WHITE))
      exit()

    print("\n{}Found {}{}{} Results:\n".format(GREEN,RED,numberOfMovies,GREEN))

    for i in range(0,len(containers)):
        print("{}{}.{}{}".format(GREEN,i+1,WHITE,containers[i].a["oldtitle"]))
      
    choice = int(input("\n{}Choose Any One Movie:{}".format(GREEN,WHITE)))
    movie_url = getMovieURL(containers,choice)
    main_url = mainURL(movie_url)
    print("\n{}URL: {}{}\n".format(GREEN,BLUE,main_url))
except Exception as e:
   print("{}No Resource Found, Try Again Later!\n{}".format(RED,e))
finally:
    input("\n{}Press Any Key To Continue....".format(GREEN))

