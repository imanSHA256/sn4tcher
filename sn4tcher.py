#!/usr/bin/python
# -*- coding: utf-8 -*- 
# Code by imanSHA256

import nmap
import requests as re
from bs4 import BeautifulSoup 
import socket
import bs4
import sys

default     = "\033[0m"
white       = '\033[97m'
green       = '\033[1;32m'
red         = '\033[1;31m'
yellow      = '\033[1;33m'
magneta     = "\033[35m"
cyan        = "\033[36m"
lgray       = "\033[37m"
dgray       = "\033[90m"
lred        = "\033[91m"
lgreen      = "\033[92m"
lyellow     = "\033[93m"
lblue       = "\033[94m"
lmagneta    = "\033[95m"
lcyan       = "\033[96m"
str_sprt="%s -------------------------------------------------------"
url=sys.argv[1]



description=yellow+""" 



 _____ _____ ___ _____ _____ _____ _____ _____ 
|   __|   | | | |_   _|     |  |  |   __| __  |
|__   | | | |_  | | | |   --|     |   __|    -|
|_____|_|___| |_| |_| |_____|__|__|_____|__|__|



"""+lblue+"https://github.com/imanSHA256"

print(description)



headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Host': 'www.shodan.io'  
}
#DNS loockup for hostname
socket_ip=socket.gethostbyname(url)
print(str_sprt % lmagneta )
print('%s Host: ' % lcyan + lyellow + socket_ip )
print(str_sprt % lmagneta )

#header info for hostname 
header_data=re.get("https://api.hackertarget.com/httpheaders/?q="+url)
print("%s HTTP Header : " % lcyan + url + " : \n")
print('%s ' % red + header_data.text )
print(str_sprt % lmagneta )

#ports by shodan
shodan_url="https://www.shodan.io/host/"+socket_ip
shodan_content=re.get(shodan_url,headers=headers)
soup=BeautifulSoup(shodan_content.text, 'lxml')
ul=soup.find("ul", class_="ports")
ports=[]
for a in ul.findAll('a', href=True):
    ports.append(a['href'].replace('#',''))
str_ports='%s ' + str(ports).replace('[','').replace(']','').replace(',','').replace('\'','')
print("%s Ports:" % cyan  + str_ports % lred)
print(str_sprt % lmagneta )

#whois info for hostname 
whois_data=re.get("https://api.hackertarget.com/whois/?q="+url)
print("%s whois lookup result for " % lcyan + url + " : \n")
print('%s ' % yellow + whois_data.text )
print(str_sprt % lmagneta )

#banner lookup
banners=re.get("https://api.hackertarget.com/bannerlookup/?q="+socket_ip)
print("%s banner lookup result for " % lcyan +socket_ip + " : \n")
print('%s ' % lgreen + banners.text + "\n" )
print(str_sprt % lmagneta )

#Reverse ip loock up
Domains=re.get("https://api.hackertarget.com/reverseiplookup/?q="+socket_ip)
print("%s reverse ip loockup result for " % lcyan +socket_ip + " : \n")
if "No DNS A records found" in Domains.text:
   print('%s ' % default + "No DNS A records found \n")
else:
   domains_list = str(Domains.text).split()
   for i in domains_list:
      print('%s ' % default + "www." + i  )










