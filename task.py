from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import pyautogui
import tkinter as tk
from tkinter import messagebox

import threading
import keyboard
import time

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Tool mời')
        self.root.geometry('400x150')
        self.is_scrolling = False

        self.info1 = tk.Label(self.root, text='BẤM PHÍM CÁCH (KHOẢNG TRẮNG) ĐỂ MỜI TỰ ĐỘNG')
        self.info1.pack(pady=10)
        self.info2 = tk.Label(self.root, text='BẤM PHÍM "x" ĐỂ DỪNG LẠI')
        self.info2.pack(pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        
        self.driver = self.start_driver()
        keyboard.add_hotkey('space', self.start_scrolling)  
        keyboard.add_hotkey('x', self.pause)  

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--guest')

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://www.facebook.com/') 

        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'pass')

        email_field.send_keys('0932140098')
        password_field.send_keys('@Duchieu#')

        login_button = driver.find_element(By.NAME, 'login')
        login_button.click()

        return driver

    def start_scrolling(self):
        if not self.is_scrolling:  
            self.is_scrolling = True
            self.scrolling_thread = threading.Thread(target=self.scroll)
            self.scrolling_thread.start()
    
    def scroll(self):
        print('---scroll---')
        self.is_scrolling = True
        while self.is_scrolling:
            elements = self.driver.find_elements(By.XPATH, "//div[@aria-label='Thêm bạn bè' and @role='button']")
            for invite_button in elements:
                self.driver.execute_script("arguments[0].style.border='3px solid red'", invite_button)
                # invite_button.click()
            
            pyautogui.scroll(-300)
            time.sleep(0.2)

    def pause(self):
        print('---pause---')
        self.is_scrolling = False


    def on_closing(self):
        if messagebox.askokcancel('TẮT', 'BẠN MUỐN TẮT ?'):
            self.driver.quit()
            self.root.destroy()   

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
