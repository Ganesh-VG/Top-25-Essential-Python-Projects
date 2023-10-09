from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

chrome_driver = Service("C:\softwares\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver, options=chrome_option)

driver.get("https://www.instagram.com/accounts/login")
time.sleep(5)
user_name = driver.find_element(By.NAME, value="username")
user_name.send_keys("<username>")
time.sleep(5)
password = driver.find_element(By.NAME, value="password")
password.send_keys("<password>")
time.sleep(5)
sign_in = driver.find_element(By.CLASS_NAME, value="_acap")
sign_in.click()
time.sleep(15)
not_now = driver.find_element(By.CSS_SELECTOR, value="._ac8f div")
not_now.click()
time.sleep(5)
no = driver.find_element(By.CLASS_NAME, value="_a9_1")
no.click()
time.sleep(10)
a = 10
while a > 0:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    like = driver.find_elements(By.CLASS_NAME, value="xp7jhwk")
    print(len(like))
    for li in like:
        time.sleep(2)
        li.click()
    a -= 1