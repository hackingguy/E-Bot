#!/usr/bin/env python3
# -.- coding: utf-8 -.-
# BollyBot.py
try:
    import os
    import re
    import sys
    import requests
    import subprocess
    import base64
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

#Search For Movies On Openloadtv.co (Soon Adding More Websites)
def search(movie_name):
    try:
        headers = {
        'authority': 'openloadtv.co',
        'accept': '*/*',
        'dnt': '1',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.61',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://openloadtv.co',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://openloadtv.co/',
        'accept-language': 'en-US,en;q=0.9'
        }
        data = "s="+movie_name+"&id=12528&post_type=movie&action=is_ajax_load_posts&page=1&security=32d4ef6611"
        myurl = 'https://openloadtv.co/wp-admin/admin-ajax.php'
        if(DEBUG==True):
            print("Search URL:{}".format(myurl))
        req = requests.post(myurl, headers=headers,data=data)
        response = req.content;
        page_html = response
        page_soup = soup(page_html,"html.parser")
        containers = page_soup.findAll("a")
        if(len(containers)!=0):
            print("\n{}Found {}{}{} Results:\n".format(GREEN,RED,len(containers),GREEN))
        else:
            print("{}No Movies Found!".format(RED))
            input("{}Press Any Key To Continue...{}".format(GREEN,WHITE))
            exit()
        return containers
    except Exception as e:
        errorOccured("search",e)

#Mixdrop URL
def getMovieURL(choice,containers):
    try:
        my_url = containers[2*(choice-1)+1]["href"]
        if(DEBUG==True):
            print("{}1st URL:{}{}".format(GREEN,WHITE,my_url))
        req = requests.get(my_url, headers=headers)
        response = req.content
        page_html = response
        page_soup = soup(page_html,"html.parser")
        containers = page_soup.findAll("iframe")
        loc=""
        try:
            if(containers[2]["src"][:5]!="https"):
                loc="https:"+containers[2]["src"]
                print("\n{}URL:{} https:{}\n".format(GREEN,BLUE,containers[2]["src"]))
            else:
                loc = containers[2]["src"];
                print("\n{}URL: {}{}\n".format(GREEN,BLUE,containers[2]["src"]))
            return loc
        except:
            try:
                containers = page_soup.findAll('a')
                loc=containers[36]["href"]
                return loc
            except:
                print("{}Resource Not Found".format(RED))
    except Exception as e:
        errorOccured("getMovieURL",e)
            
#Unpack Hidden CDN URLS
def unpacker(data):
    try:
        def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
            return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])
        def unpack(p, a, c, k, e=None, d=None):
            while (c):
                c-=1
                if (k[c]):
                    p = re.sub("\\b" + baseN(c, a) + "\\b",  k[c], p)
            return p
        encrypted = r'''{}'''.format(data.split("\n")[3])
        encrypted = '(' + encrypted.split('}(')[1][:-1]
        result = eval('unpack' + encrypted)
        loc = "http:"+result.split(";")[2].split("\"")[1]
        return loc
    except Exception as e:
        errorOccured("unpacker",e)
 
def bypass_shortURLS(short_url):
  try:
      if "mixdrop" not in short_url:
        base64_encoded_url = short_url.split("url=")[1].split("&type=")[0]
        main_url = base64.b64decode(base64_encoded_url)
        return main_url
      else:
        return short_url
  except Exception as e:
        errorOccured("bypass_shortURLS",e)

#Uses Unpacker And Get Main CDN Link
def removeAds_getCDN(movie_url):
    try:
        if "mixdrop" in movie_url:
            #These Were Not Useful Now Previously There Was A HTML Redirection
            #r = requests.get(movie_url,headers=headers)
            #new_url = movie_url.split("/e/")[0]+str(r.content).split("window.location = \"")[1].split("\";")[0]
            movie_url = movie_url.replace("/f/","/e/")
            if(DEBUG==True):
                print("{}2nd URL:{}{}".format(GREEN,WHITE,main_url))
            r = requests.get(movie_url,headers=headers)
            res = r.content
            htmlData = soup(res,"html.parser")
            scriptTags = htmlData.findAll('script')
            if(DEBUG==True):
              for i in range(0,len(scriptTags)):
                print("{}{}. JavaScript:{}\n\n{}\n\n".format(GREEN,i,WHITE,scriptTags[i]))
            packedJavaScript = str(scriptTags[7])
            return unpacker(packedJavaScript)
        else:
            return movie_url
    except Exception as e:
        errorOccured("removeAds_getCDN",e)

#Start VLC as SubProcess
def startVLC(link):
    try:
        if(sys.platform=="win32"):
          p = subprocess.Popen([os.path.join("C:/", "Program Files", "VideoLAN", "VLC", "vlc.exe"),link])
        else:
          p = subprocess.Popen(["vlc",link])
    except Exception as e:
        print("{}VLC Not Found And Please Note That Link Will not work without EBOT Session\nIf Present Please Check Environmental Variables{}".format(RED,GREEN))

#Main
if(__name__=="__main__"):
    try:
        if(DEBUG==False):
            heading()
        movie_name="+".join(input("\n{}Enter Name Of Movie:{}".format(GREEN,WHITE)).split())
        containers=search(movie_name)
        for i in range(0,int(len(containers)/2)):
            name =' '.join(str(containers[2*i+1]["href"]).split("/")[-2].split("-"))
            print("{}{}.{}{}".format(GREEN,i+1,WHITE,name))
        choice = int(input("\n{}Choose Any One Movie:{}".format(GREEN,WHITE)))
        movie_url = getMovieURL(choice,containers)
        main_url = bypass_shortURLS(movie_url)
        if(DEBUG==True):
          print("{}Unshorten URL:{}{}".format(GREEN,WHITE,main_url))
        cdnLink = removeAds_getCDN(main_url)
        print("\n{}URL:{} {}\n".format(GREEN,BLUE,cdnLink))
        startVLC(cdnLink)
    except Exception as e:
        if(DEBUG==True):
            print("{}Something Fishy, Try Again Later!\n{}".format(RED,e))
        else:
            print("{}Sorry For Issue!".format(RED))
    
    finally:
        input("\n{}Press Enter To Continue....".format(GREEN))