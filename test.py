from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import pyautogui
import tkinter as tk
from tkinter import ttk
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
        self.scrolling_thread = None

        self.info1 = tk.Label(self.root, text='BẤM PHÍM CÁCH (KHOẢNG TRẮNG) ĐỂ MỜI TỰ ĐỘNG')
        self.info1.pack(pady=5)
        self.info2 = tk.Label(self.root, text='BẤM PHÍM "x" ĐỂ DỪNG LẠI')
        self.info2.pack(pady=5)

        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        
        self.driver = self.start_driver()
        # self.keyboard_thread = threading.Thread(target=self.listen_keyboard, daemon=True)
        # self.keyboard_thread.start()
        keyboard.add_hotkey('space', self.start_scrolling)  
        keyboard.add_hotkey('x', self.pause)  

        self.delay_time = tk.DoubleVar()
        self.delay_time.set(0.2)

        self.radio1 = tk.Radiobutton(root, text="Chậm", variable=self.delay_time, value=1)
        self.radio2 = tk.Radiobutton(root, text="Vừa", variable=self.delay_time, value=0.5)
        self.radio3 = tk.Radiobutton(root, text="Nhanh", variable=self.delay_time, value=0.2)
        # self.radio3 = tk.Radiobutton(root, text="Nhanh", variable=self.scrolling_speed, value=2, command=self.on_select)

        # Pack the radio buttons on the window
        self.radio1.pack(pady=5)
        self.radio2.pack(pady=5)
        self.radio3.pack(pady=5)


    def on_select(self):
        selected = self.delay_time.get()  # Get the current value of the selected radio button
        print(f"You selected: {selected}")

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--guest')

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('https://vi.wikipedia.org/wiki/Danh_s%C3%A1ch_nguy%C3%AAn_th%E1%BB%A7_qu%E1%BB%91c_gia_Belarus') 

        # email_field = driver.find_element(By.NAME, 'email')
        # password_field = driver.find_element(By.NAME, 'pass')

        # email_field.send_keys('0932140098')
        # password_field.send_keys('@Duchieu#')

        # login_button = driver.find_element(By.NAME, 'login')
        # login_button.click()

        return driver

    def start_scrolling(self):
        if not self.is_scrolling:  
            self.is_scrolling = True
            self.scrolling_thread = threading.Thread(target=self.scroll)
            self.scrolling_thread.start()

    def scroll(self):
        print('---scroll---', self.is_scrolling )
        while self.is_scrolling:
            # elements = self.driver.find_elements(By.XPATH, "//div[@aria-label='Thêm bạn bè' and @role='button']")
            # for invite_button in elements:
            #     self.driver.execute_script("arguments[0].style.border='3px solid red'", invite_button)
                # invite_button.click()
            
            pyautogui.scroll(-200)
            time.sleep(self.delay_time.get())

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
