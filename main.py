import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service("/Users/souravmohile/Development/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

MAIL = os.environ["MAIL"]
PASSWORD = os.environ["PASSWORD"]

driver.get("https://bumble.com/en-in/")

sign_in = driver.find_element_by_xpath("//*[@id='page']/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a")
sign_in.click()

time.sleep(2)

facebook = driver.find_element_by_css_selector(".button__text span")
facebook.click()

time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

mail = driver.find_element_by_xpath("//*[@id='email']")
mail.send_keys(MAIL)
password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys(PASSWORD)

login = driver.find_element_by_css_selector("#buttons input")
login.click()

driver.switch_to.window(base_window)

time.sleep(10)

dislike = driver.find_element_by_xpath("//*[@id='main']/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span")

for _ in range(10):
    time.sleep(2)
    dislike.click()








