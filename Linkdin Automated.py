pip install selenium
pip install beautifulsoup4
import os,random,sys,time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Chrome('driver/chromedriver.exe')
browser.get('https://www.linkedin.com/uas/login')
file=open('config.txt')
lines=file.readlines()
username=lines[0]
password=lines[1]
elementID=browser.find_element_by_id('username')
elementID.send_keys(username)
elementID=browser.find_element_by_id('password')
elementID.send_keys(password)
elementID.submit()
visitingProfileID='/in/kushankur-das-6b2655191/'
fullLink='https://www.linkedin.com/'+visitingProfileID
browser.get(fullLink)