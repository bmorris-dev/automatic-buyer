from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome('C:/Users/barrett/Desktop/chromedriver.exe')
driver.get('https://achingcriminalbytes.bmorris.repl.co/')
driver.fullscreen_window()
button = driver.find_element("xpath", "/html/body/button")
button.click()
time.sleep(10000)
