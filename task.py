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
        self.info1 = tk.Label(self.root, text='BẤM PHÍM CÁCH (KHOẢNG TRẮNG) ĐỂ MỜI TỰ ĐỘNG')
        self.info1.pack(pady=10)
        self.info2 = tk.Label(self.root, text='BẤM PHÍM "x" ĐỂ DỪNG LẠI')
        self.info2.pack(pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        
        self.driver = self.start_up()
        self.keyboard_thread = threading.Thread(target=self.start_key_listener, daemon=True)
        self.keyboard_thread.start()

    def start_up(self):
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
    
    def start_key_listener(self): 
        while self.root.winfo_exists():
            if keyboard.is_pressed('space'):
                self.start_scrolling()

    def start_scrolling(self):
        print('---scroll---')
        for _ in range (20):
            pyautogui.scroll(-300)
            time.sleep(0.2)

    def on_closing(self):
        if messagebox.askokcancel('TẮT', 'BẠN MUỐN TẮT ?'):
            self.driver.quit()
            self.keyboard_thread.join()
            self.root.destroy()   

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
