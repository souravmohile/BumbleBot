# Imports
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from transformers import pipeline

# ChromeDriver setup
ser = Service("/Users/souravmohile/Development/chromedriver")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# Bumble login credentials
MAIL = os.environ["MAIL"]
PASSWORD = os.environ["PASSWORD"]

# Navigate to the Bumble website
driver.get("https://bumble.com/en-in/")

# Clcik on the sign in button
sign_in = driver.find_element_by_xpath("//*[@id='page']/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a")
sign_in.click()

# Wait for the sign-in page to load
time.sleep(2)

# Clcik on the "Continue with Facebook" button
facebook = driver.find_element_by_css_selector(".button__text span")
facebook.click()

# Wait for the login window to load
time.sleep(2)

# Set focus on Facebook login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Enter credentials
mail = driver.find_element_by_xpath("//*[@id='email']")
mail.send_keys(MAIL)
password = driver.find_element_by_xpath("//*[@id='pass']")
password.send_keys(PASSWORD)

# Click the login button
login = driver.find_element_by_css_selector("#buttons input")
login.click()

# Switch back to bumble window
driver.switch_to.window(base_window)

# Wait for the page to load
time.sleep(10)

# Find the dislike button
like = driver.find_element_by_xpath("//*[@id='main']/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[2]/span")
dislike = driver.find_element_by_xpath("//*[@id='main']/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span")

# Like or Dislike the first 30 profiles based on the sentiment of the bio text.
bio_text = driver.find_element_by_xpath("//*[@id='main']/div/div[1]/main/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span").text
for _ in range(30):
    time.sleep(2)
    sentiment_analyzer = pipeline("sentiment-analysis")
    bio_sentiment = sentiment_analyzer(bio_text)
    if bio_sentiment[0]['label'] == 'POSITIVE':
        like.click()
    else:
        dislike.click()
