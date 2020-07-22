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
    hdr = { 'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0' }
    req = requests.get(myurl, headers=hdr)
    response = urllib.request.urlopen(req, timeout=4)
    page_html = response.read()
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("div",{"class":"featuredItems singleVideo"})
    return containers

def getMovieURL(containers,choice):
    movie_url = "https://fmovies.top/movies/"+"-".join((containers[choice-1].a["oldtitle"]).split())+"/"
    req = urllib.request.Request(movie_url, headers=hdr)
    response = urllib.request.urlopen(req, timeout=4)
    page_html = response.read()
    page_soup = soup(page_html,"lxml")
    containers = page_soup.findAll("a",{"class":"thumb mvi-cover"})
    movie_url = containers[0]["href"]
    return movie_url

def mainURL(movie_url):
    req = urllib.request.Request(movie_url, headers=hdr)
    response = urllib.request.urlopen(req, timeout=4)
    page_html = response.read()
    page_soup = soup(page_html,"lxml")
    containers = page_soup.findAll("iframe",{"class":"metaframe rptss"})
    return containers[0]["src"]

try:
    heading()
    containers = search("+".join((input("\n{}Enter Movie Name:{}".format(GREEN,WHITE))).split()))
    print("\n{}Found {}{}{} Results:\n".format(GREEN,RED,len(containers),GREEN))

    for i in range(0,len(containers)):
        print("{}{}.{}{}".format(GREEN,i+1,WHITE,containers[i].a["oldtitle"]))
      
    choice = int(input("\n{}Choose Any One Movie:{}".format(GREEN,WHITE)))
    movie_url = getMovieURL(containers,choice)
    main_url = mainURL(movie_url)
    print("\n{}URL: {}{}\n".format(GREEN,BLUE,main_url)
except:
    print("{}No Resource Found, Try Again Later!".format(RED))