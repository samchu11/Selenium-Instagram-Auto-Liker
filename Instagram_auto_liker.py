import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def main():

    id = '{your_instagram_ID}'
    passd = '{your_instagram_password}'
    browser_locale = 'en'
    try:
        url = 'https://www.instagram.com'
        targetURL ='{target_instagram_URL}'
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        chrome_options.add_argument("--lang={}".format(browser_locale))
        chrome_options.add_experimental_option("prefs",prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)

        # resize browser window to maximize_window
        driver.maximize_window()

        username = driver.find_element_by_name('username')
        username.send_keys(id)

        password = driver.find_element_by_name('password')
        password.send_keys(passd)
        time.sleep(1)

        password.send_keys(Keys.ENTER)
        time.sleep(1)

        driver.get(targetURL)
        first_picture(driver)
        like_pic(driver) 
        continue_liking(driver)

        # Close the tab/browser when done
        Driver.CloseDriver()
    except:
        print "error"

def first_picture(driver): 
        # finds the first picture  
        time.sleep(0.5)
        pic = driver.find_element_by_class_name("_9AhH0")
        time.sleep(0.5)
        pic.click()   # clicks on the first picture 

def next_picture(driver): 
    time.sleep(0.5)
    nex = driver.find_element_by_xpath('//a[@class=" _65Bje  coreSpriteRightPaginationArrow"]')
    return nex

def like_pic(driver): 
    time.sleep(1) 
    like = driver.find_element_by_xpath('//div[@class="QBdPU "]/*[name()="span"]/*[name()="svg"][@aria-label="Like"]')
    time.sleep(1) 
    # clicking the like button
    like.click()   

def continue_liking(driver): 
    while True: 
        next_el = next_picture(driver) 
  
        # if next button is there then 
        if next_el != False:   
  
            # click the next button 
            next_el.click()    
            time.sleep(1) 
  
            # like the picture 
            like_pic(driver)            
        else: 
            print("not found")  
            break

main()

#bug/issue found
#1. if post already been liked, will like the first comment
#2. if post already beem liked and no comment, program exit with error
#3. Not support 2FA enabled account
#4. default language is set to 'en', which will affect the "Like" button content `[@aria-label="Like"]`
http://chromedriver.chromium.org/downloads
https://github.com/sameerkumar18/Instagram-Auto-Liker
https://github.com/davidteather/Instagram-Bot

Selenium-Instagram-Auto-Liker