from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import requests
import time
from datetime import datetime
import wget
import os

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=chrome_options)

driver.get("http://www.facebook.com")

username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
submit   = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

username.send_keys(#insert username#)
password.send_keys(#insert password#)

submit.click()

time.sleep(3)

driver.get(#insert photos page link#)

while True:
	time.sleep(5)
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
	try:
		driver.find_element_by_xpath('//div[@data-pagelet="ProfileAppSection_{n}"]/div/div/div/div/div/div/div/div/h2/span/a')
	except: continue
	else: break

#declare images array to hold src and filename
images = []

#target all the link elements on the page
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
#narrow down all links to image links only
anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]

print('Found ' + str(len(anchors)) + ' links to images')

#extract the [0]th image element in each link
counter = 0
for a in anchors:
	driver.get(a)
	time.sleep(5)
	img = driver.find_elements_by_tag_name("img")

	#get source image link
	pic_link = img[0].get_attribute("src")

	#get photo upload date
	dates = driver.find_elements_by_tag_name("a")

	#if upload date isn't able to be retrieved, assign counter as unique filename
	while True:
		try:
			upload_date = datetime.strptime(dates[11].get_attribute("aria-label"), "%B %d, %Y")
			filename = upload_date.strftime("%d-%b-%Y") + " (" + str(counter) + ")"
			break
		except:
			filename = "(" + str(counter) + ")"
			break

	images.append((pic_link, filename))

	counter1 += 1

path = #insert target directory for photos#

#save image at target location using stored filename in position 1 of image
for image in images:
    save_as = os.path.join(path, image[1] + '.jpg')
    wget.download(image[0], save_as)
    counter += 1
