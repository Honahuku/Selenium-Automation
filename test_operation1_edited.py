# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox()
# Test name: operation1
# Step # | name | target | value
# 1 | open | /reserveApp_Renewal/ | 
driver.get("http://example.selenium.jp/reserveApp_Renewal/")
# 2 | setWindowSize | 550x765 | 
driver.set_window_size(550, 765)
# 3 | runScript | window.scrollTo(0,144) | 
driver.execute_script("window.scrollTo(0,144)")
# 4 | click | id=datePick | 
driver.find_element(By.ID, "datePick").click()
# 5 | click | css=tr:nth-child(5) > .day:nth-child(5) | 
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(5) > .day:nth-child(5)").click()
# 6 | click | id=reserve_info | 
driver.find_element(By.ID, "reserve_info").click()
# 7 | click | id=guestname | 
driver.find_element(By.ID, "guestname").click()
# 8 | type | id=guestname | hoge
driver.find_element(By.ID, "guestname").send_keys("hoge")
# 9 | click | id=agree_and_goto_next | 
driver.find_element(By.ID, "agree_and_goto_next").click()
# 10 | click | id=commit | 
driver.find_element(By.ID, "commit").click()
# 11 | close |  | 
#driver.close()