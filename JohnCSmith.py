from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import csv

#configure selenium webdriver
#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--incognito')
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

#selenium to load full dynamic webpage of followers
browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver')
browser.get('https://soundcloud.com/krabbesonntagsinstitut/following')

while True:
	browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
	time.sleep(3)
	try:
		browser.find_element_by_css_selector('div.loading.regular.m-padded')
	except: break

#BeautifulSoup to load, parse, and restructure html data
html = browser.page_source.encode('utf-8')


soup = BeautifulSoup(html, 'lxml')

#load subgroup of user-list
excerpt = soup.find('ul', attrs={'class' : 'lazyLoadingList__list sc-list-nostyle sc-clearfix'})

#declare array to hold followers
#following = []

#file = open('following.csv','wb')
#writer = csv.writer(file)

#writer.writerow(['Artist Name', 'Link'])

#iterate through each a in li to extract artistname and link, populate into array
#for li_tag in excerpt.find_all("li"):
for a_tag in excerpt.find_all("a", attrs ={'class' : 'userBadgeListItem__heading sc-type-small sc-link-dark sc-truncate'}):
	artistname = a_tag.get_text().strip()
	link = "http://soundcloud.com" + a_tag.get('href')
#	following.append(artistname.encode('utf-8'),link.encode('utf-8'))
	print artistname + ' ' + link
#	writer.writerow([artistname.encode('Latin1'),link.encode('utf-8')])
#	writer.writerow([artistname,link])

#file.close
	
#print to csv
#with open('following', 'wb') as myfile:
#	wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
#	wr.writerow(following)
