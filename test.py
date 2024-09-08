from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import pyautogui
import pygetwindow as gw


import threading
import keyboard
import time


user_data_dir = "C:/Users/trthd/AppData/Local/Google/Chrome/User Data"
profile_dir = "Profile 3"
chrome_options = Options()
chrome_options.add_argument("--guest")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://github.com/SeleniumHQ') 

stop = None
while (stop!="yes"):
    span_element = driver.find_element(By.XPATH, "//span[@class='repo' and text()='selenium']")
    driver.execute_script("arguments[0].style.border='3px solid red'", span_element)

    window = gw.getWindowsWithTitle(driver.title)[0]
    window.maximize()
    w_x, w_y = window.left, window.top

    element_location = span_element.location
    e_x, e_y = element_location['x'], element_location['y']
    print("window title:", driver.title)
    print("top-left window position:",window.left, window.top)
    print("element w-position:",e_x, e_y)

    pyautogui.moveTo(w_x+e_x, w_y+e_y,duration=1)
    print("mouse position", pyautogui.position())

    stop = input("stop?")


driver.quit()