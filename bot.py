from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver import ActionChains
#from selenium_move_cursor.MouseActions import move_to_element_chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from time import sleep


#chooses between the first and second website
option = input('Would you like to do option 1 or 2: ')
valid = False
try:
    option = int(option)
    if option == 1 or option == 2:
        valid = True
except:
    while valid == False:
        try:
            option = int(option)
            if option == 1 or option == 2:
                valid = True
            else:
                option = input('Please enter either 1 or 2: ')
        except:
            option = input("Error. Please try again: ")

#this is the driver in which the program will control
driver = webdriver.Chrome('./chromedriver.exe')



#typing speed test type #1
if option == 1:
    driver.get('https://www.livechat.com/typing-speed-test/#/')
    time.sleep(2)
    start = time.time()
    end = time.time()
    timeElapsed = end - start

    while timeElapsed <= 59:
        wordElement = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/span/div[2]/span/div/div[2]/div/span[1]')
        actions = ActionChains(driver)
        actions.send_keys(wordElement.text + ' ')
        actions.perform()





#typing speed test type #2
if option == 2:
    driver.get('https://typing-speed-test.aoeu.eu/?lang=en')
    time.sleep(2)

    start = time.time()
    end = time.time()
    timeElapsed = end - start

    inputBar = driver.find_element_by_xpath('//*[@id="input"]')

    while timeElapsed <= 59:
        temp = driver.find_element_by_class_name('currentword')
        inputBar.send_keys(temp.text + ' ')
        #end = time.time()
        #timeElapsed = end-start 