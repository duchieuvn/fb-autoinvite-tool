from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import pyautogui
import tkinter as tk
from tkinter import messagebox

import os
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
        threading.Thread(target=self.keyboard_listener, daemon=True).start()

    def load_default_gui(self):
        pass

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

    def scroll_to_invite(self):
        while self.keep_running:
            try:
                elements = self.driver.find_elements_by_xpath("//div[@aria-label='Mời' and @role='button']")
                for element in elements:
                    self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
                time.sleep(0.2)

            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)

        print("Scrolling stopped.")

    def start_scrolling(self):
        if not self.keep_running:
            self.keep_running = True
            self.scrolling_thread = threading.Thread(target=self.scroll_to_invite)
            self.scrolling_thread.start()
            # self.status_label.config(text="Scrolling started...")

    def stop_scrolling(self):
        self.keep_running = False
        if self.scrolling_thread:
            self.scrolling_thread.join()
            # self.status_label.config(text="Scrolling stopped.")


    def keyboard_listener(self):
        keyboard.add_hotkey('space', self.start_scrolling)
        keyboard.add_hotkey('x', self.stop_scrolling)

    def on_closing(self):
        if messagebox.askokcancel('TẮT', 'BẠN MUỐN TẮT ?'):
            self.driver.quit()
            self.root.destroy()  

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
