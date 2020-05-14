# -*- coding: utf-8 -*-
###############################################################
# Name: Zoë Webb-Mack
# UNI: zwm2104
# ENGI-1006 Final
#
# File creates function for scraping urls from website.  Function
# called in app.py to create page of url addresses.
###############################################################

def link_scrape(http):
    '''Function scrapes webpage for urls, returns a list of
        urls formatted for html printing'''

    #import libraries
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    #open and read url
    url = urlopen(http).read()
    soup = BeautifulSoup(url)
    
    #iterate over each line, extract url from line
    urls = []
    for line in soup.find_all('a'):
        
        #format for html
        url_print = "<p><a>{}</a></p>".format(line.get('href'))
        
        #append to list
        urls.append(url_print)
    
    #join items of list    
    full_url_html = "".join(urls)

    return full_url_html
    
        