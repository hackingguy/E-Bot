#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# AnimeBot.py
try:
    import os
    import sys
    import html
    import time
    import requests
    from bs4 import BeautifulSoup as soup
except Exception as e:
    print(e)
    exit()

try:
    os.system("mkdir Animes")
except:
    pass

#Debug
DEBUG=False

#Websites Don't Allow To Enter If You Don't Use Good Headers
#I Love Apple Headers (Macintosh), Even I don't have one till now :)>
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#Shell GUI I Love it!
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END,TICK,CROSS = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\u2713', '\u274c'

#Display Heading
def heading():
    spaces = " " * 76
    print('\033c')
    sys.stdout.write(GREEN + spaces + """
                 ▄▄▄·  ▐ ▄ ▪  • ▌ ▄ ·. ▄▄▄ .    ▄▄▄▄·       ▄▄▄▄▄
                ▐█ ▀█ •█▌▐███ ·██ ▐███▪▀▄.▀·    ▐█ ▀█▪▪     •██  
                ▄█▀▀█ ▐█▐▐▌▐█·▐█ ▌▐▌▐█·▐▀▀▪▄    ▐█▀▀█▄ ▄█▀▄  ▐█.▪
                ▐█ ▪▐▌██▐█▌▐█▌██ ██▌▐█▌▐█▄▄▌    ██▄▪▐█▐█▌.▐▌ ▐█▌·
                 ▀  ▀ ▀▀ █▪▀▀▀▀▀  █▪▀▀▀ ▀▀▀     ·▀▀▀▀  ▀█▄▀▪ ▀▀▀ 
    """ + END + BLUE +
    '\n' + '{}Download Any Anime You Want ({}Anime Bot{}){}'.format(YELLOW, RED, YELLOW, BLUE).center(98) +
    '\n' + 'Made With <3 by: {0}Hacking Guy'.format(YELLOW).center(86) +
    '\n' + 'Version: {}1.0{} \n'.format(YELLOW, END).center(86))

#Error Handling
def errorOccured(fun_name,e):
    if(DEBUG==False):
            print("{}May Be There Is Problem\nCheck Internet Connection Or Report Us Issue at https://github.com/hackingguy/E-Bot/Issues".format(RED))
            exit()
    else:
            print("Exception Occured:\nFunction:{}\n{}".format(fun_name,e))

#Generate A HTML File
def generateHTML(links):
    try:
        file = "Animes/"+name+".html"
        k= open(file,"w")
        k.write("<html lang=\"en\" dir=\"ltr\"> <head> <meta charset=\"utf-8\"> <title></title> </head> <style>*{background:black;font-size:60px}.slide-in-left{color:white;-webkit-animation:slide-in-left .5s cubic-bezier(.25,.46,.45,.94) both;animation:slide-in-left .5s cubic-bezier(.25,.46,.45,.94) both}.Link{margin:5px;color:white;animation-delay:1s;border-radius:2.5px;-webkit-animation:slide-in-left .5s cubic-bezier(.25,.46,.45,.94) both;animation:slide-in-left .5s cubic-bezier(.25,.46,.45,.94) both}@-webkit-keyframes slide-in-left{0%{-webkit-transform:translateX(-1000px);transform:translateX(-1000px);opacity:0}100%{-webkit-transform:translateX(0);transform:translateX(0);opacity:1}}@keyframes slide-in-left{0%{-webkit-transform:translateX(-1000px);transform:translateX(-1000px);opacity:0}100%{-webkit-transform:translateX(0);transform:translateX(0);opacity:1}}</style> <body><h1 class=\"slide-in-left\">Made With <3 By Hacking Guy :-</h1><br>\n")
        for i in range(0,len(links)):
            k.write("<a class=\"Link\" href=\""+links[i]+"\">Episode "+str(i+1)+"</a><br><br>\n")
        k.write("</body></html>")
        k.close()
    except Exception as e:
        errorOccured("search",e)
    
#Search Anime
def search(anime):
    try:
        string = "https://gogoanime.video//search.html?keyword="+("%20").join(anime.split())
        if(DEBUG==True):
            print("URL: {}".format(string))
        req = requests.get(string,headers=headers)
        page_html = req.content
        page_soup = soup(page_html,"html.parser")
        containers = page_soup.findAll("div",{"class":"last_episodes"})
        result = list(containers[0].ul)
        result = list(filter(('\n').__ne__, result))
        animes_names=[]
        if(len(result)==0):
            print("No Anime Found")
            exit()
        for i in range(0,len(result)):
            string =BLUE+str(i+1)+"."+WHITE+result[i].p.a['href'][10:].capitalize()
            animes_names.append(" ".join(string.split("-")))
        return [animes_names,result]
    except Exception as e:
        errorOccured("search",e)

#Get Anime From Website gogoanime.video
def getAnime(animes_pack,start,end,choice):
    try:
        name = animes_pack[1][choice-1].p.a['href'][10::]
        name = name.lower()
        url="https://gogoanime.video/"
        url=url+name+"-episode-"
        anime_links = []
        for i in range(start,end+1):
            print("{}Episode {}{} {}Extracted".format(GREEN,RED,i,GREEN),end="")
            my_url = url+str(i) 
            anime_links.append(ExtractEpisode(my_url))
            sys.stdout.flush()
        return anime_links
    except Exception as e:
        errorOccured("ExtractEpisode",e)
    
#Extract Episode
def ExtractEpisode(my_url):
    try:
        req = requests.get(my_url, headers=headers)
        if(DEBUG==True):
            print("URL: {}".format(my_url))
        page_html = req.content
        page_soup = soup(page_html,"html.parser")
        containers = page_soup.find("iframe")
        string="https:"+str(html.unescape(containers['src']))
        string=string.replace("streaming.php","loadserver.php",1)
        if(DEBUG==True):
            print("URL: {}".format(string))
        url = requests.get(string,headers=headers)
        response = url.content
        for i in range(0,10):
                print(".",end="")
                sys.stdout.flush()
                time.sleep(0.01)
        try:
            html_soap = soup(response,"html.parser")
            main_url = str(html_soap.findAll("script")[2]).split("sources:[{file: '")[1].split("',label:")[0]
            print("{}{}".format(GREEN,TICK))
            return main_url
        except Exception as e:
            if(DEBUG==False):
                print("{}{}".format(RED,CROSS))
            else:
                print("{}{}{}".format(RED,CROSS,e))
                return "Not Found"
    except Exception as e:
        if(DEBUG==False):
                print("{}{}".format(RED,CROSS))
        else:
            print("{}{}{}".format(RED,CROSS,e))
        return "Not Found"

if __name__=="__main__":
    try:
        if(DEBUG==False):
            heading()
        name= input("\n{}Name Of Anime:{}".format(GREEN,WHITE).ljust(20," "))
        animes_pack = search(name)
        print("\n{}Found {}{}{} Results:\n".format(GREEN,RED,len(animes_pack[0]),GREEN))
        for i in range(0,len(animes_pack[0])):
            print("{}".format(animes_pack[0][i]))
        choice = int(input("\n{}Choose Anyone:{}".format(GREEN,WHITE)))
        start = int(input("\n{}Enter Starting Of Episodes:{}".format(GREEN,WHITE)))
        end = int(input("{}Enter Ending Of Episodes:{}".format(GREEN,WHITE)))
        print("\n{}Starting Extraction....".format(GREEN))
        links = getAnime(animes_pack,start,end,choice)
        print("\n{}Extraction Done".format(GREEN))
        generateHTML(links)
    except Exception as e:
        if(DEBUG==True): 
            print("Error \n{}".format(e))
        else:
            print("Sorry For The Issue")
    
    finally:
        input("Press Any Key To Continue")
