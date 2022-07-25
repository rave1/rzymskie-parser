from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from parse import parse
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

REVIEW_COUNT = 10

url = 'https://www.google.pl/maps/place/Rzymskie+Wakacje/@50.6668753,17.9184083,17z/data=!3m1!4b1!4m5!3m4!1s0x4710530384fecafd:0x3950c861f0f77d6e!8m2!3d50.6668719!4d17.920597'
driver.get(url)
driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div/div[1]/span[1]/span/span[1]/span[2]/span[1]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[9]/button').click()
driver.find_element(By.XPATH, '//*[@id="action-menu"]/ul/li[4]').click()
time.sleep(2)

#Find scroll layout
scrollable_div = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]')
#Scroll as many times as necessary to load all reviews
for i in range(0, REVIEW_COUNT):
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', 
                scrollable_div)
        time.sleep(1)

PAGE_SOURCE = driver.page_source
# Parse reviews
parse(PAGE_SOURCE)


time.sleep(10)