from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument(r"--user-data-dir=C:/Users/user/AppData/Local/Google/Chrome/User Data")


CHROME_DRIVER_PATH = 'YOUR CHROME DRIVER PATH'
SERVICE = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=  SERVICE)

driver.get("https://www.instagram.com/")
time.sleep(3)
# -------------LOGIN INSTAGRAM---------
MY_PASSWORD = 'your password'
MY_USERNAME = "your useername/email"
SIMILAR_ACCOUNT = "instagram acccount to search"


USERNAME = driver.find_element(By.NAME, "username")
USERNAME.send_keys(MY_USERNAME)
PASSWORD = driver.find_element(By.NAME, "password")
PASSWORD.send_keys(f"{MY_PASSWORD}")
PASSWORD.send_keys(Keys.ENTER)
time.sleep(5)
# turn notifications off
try:
    driver.find_element(By.CLASS_NAME, "_a9_1").click()
except:
    pass
else:
    time.sleep(3)

# ---------------------------------------------------
open_search_bar = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div')
open_search_bar.click()
time.sleep(2)
# ---------------Find instagram account
search = driver.find_element(By.CLASS_NAME, "_aauy")
search.send_keys(SIMILAR_ACCOUNT)
time.sleep(3)
search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)
time.sleep(5)
# ---------------SEARCH FOLLOWERS-------------
followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers.click()
time.sleep(4)
# -------------FOLLLOW acoount's FOLLOWERS FOR 20 SECONDS

twenty_seconds = time.time() + 20

while time.time() <= twenty_seconds:
    all_followers = driver.find_elements(By.CLASS_NAME, "_acas")
    for follower in all_followers:
        try:
            follower.click()
            time.sleep(2)
        except:
            pass
        else:
            if time.time() <= twenty_seconds:
                break