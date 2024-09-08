from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import pyautogui

import os
import threading
import keyboard
import time

chrome_options = Options()
chrome_options.add_argument("--guest")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.facebook.com/') 
        
keep_running = False
scrolling_thread = None

def scroll_to_invite():
    global keep_running
    while keep_running:
        try:
            if not keep_running:
                break

            elements = driver.find_elements(By.XPATH, "//div[@aria-label='Mời' and @role='button']")
            for invite_button in elements:
                # driver.execute_script("arguments[0].style.border='3px solid red'", invite_button)
                invite_button.click()

            pyautogui.scroll(-300)
            time.sleep(0.1)

        except NoSuchElementException:
            print('NOT FOUND')
            time.sleep(1)
            continue

        except StaleElementReferenceException:
            print('STALE ELEMENT')
            time.sleep(1)
            continue

    print("Scrolling stopped.")

def start_scrolling():
    global keep_running, scrolling_thread
    if not keep_running:  
        os.system('cls')
        print('---ĐANG LƯỚT ĐỂ MỜI---')
        print('----------------------')
        print('BẤM PHÍM "x" ĐỂ DỪNG LẠI')
        keep_running = True
        scrolling_thread = threading.Thread(target=scroll_to_invite)
        scrolling_thread.start()

def stop_scrolling():
    global keep_running
    if keep_running:
        keep_running = False
        if scrolling_thread:
            scrolling_thread.join()  

def stop_program():
    stop_scrolling()
    os.system('cls')
    print('--------ĐÃ DỪNG QUÁ TRÌNH MỜI TỰ ĐỘNG----------')
    print('-----------------------------------------------')
    print('BẤM PHÍM CÁCH (KHOẢNG TRẮNG) ĐỂ BẮT ĐẦU MỜI TỰ ĐỘNG')
    print('BẤM PHÍM "ESC" ĐỂ THOÁT TOOL')

# Set up hotkeys
def main():
    os.system('cls')
    print('BẤM PHÍM CÁCH (KHOẢNG TRẮNG) ĐỂ BẮT ĐẦU MỜI TỰ ĐỘNG')
    print('BẤM PHÍM "ESC" ĐỂ THOÁT TOOL')

    keyboard.add_hotkey('space', start_scrolling)  
    keyboard.add_hotkey('x', stop_program) 

    while not keyboard.is_pressed('esc'):
        keyboard.wait('esc')

    driver.quit()

main()
