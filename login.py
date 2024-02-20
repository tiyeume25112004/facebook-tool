from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from time import sleep
import re

Edge_option = Options()
# Edge_option.add_argument("--headless")
Edge_option.add_argument("--disable-infobars")
Edge_option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=Edge_option)

driver.get("http://facebook.com")
print("Openning...")
email = input("Enter your email: ")
password = input("Enter your password: ")

emailUser = driver.find_element(by=By.NAME, value="email")
passwordUser = driver.find_element(by=By.NAME, value="pass")
button = driver.find_element(By.XPATH, "//button[@class='_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy']")
emailUser.send_keys("akazotaalhayamala@gmail.com")
passwordUser.send_keys("akazotooablahahaha")
# emailUser.send_keys(email)
# passwordUser.send_keys(password)

button.click()

fullPage = driver.page_source
# text_box = driver.find_element()
