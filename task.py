from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

import pyautogui
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox

import threading
import keyboard
import time

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title('FacebookAutoTool@duchieuvn')
        self.root.geometry('400x200')
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)
        self.icon = PhotoImage(file="icon.png")  
        self.root.iconphoto(True, self.icon)
        self.config_ui()

        self.is_scrolling = False
        self.scrolling_thread = None
        threading.Thread(target=self.start_driver).start()

        keyboard.add_hotkey('space', self.start_scrolling)  
        keyboard.add_hotkey('x', self.pause)  

    def config_ui(self):
        self.img_path = PhotoImage(file="img.png")
        self.bg = tk.Label(self.root, image=self.img_path, width=450, height=300)
        self.bg.place(relheight=1, relwidth=1)

        self.info1 = tk.Label(self.root, text='BẤM PHÍM CÁCH (KHOẢNG TRẮNG) ĐỂ MỜI TỰ ĐỘNG', font='Arial 10')
        self.info2 = tk.Label(self.root, text='BẤM PHÍM "x" ĐỂ DỪNG LẠI', font='Arial 10')
        self.info1.pack(padx=5, pady=(5,0), anchor="w")
        self.info2.pack(padx=5, pady=0, anchor="w")


        self.delay_time = tk.DoubleVar()
        self.delay_time.set(0.2)

        self.radio1 = tk.Radiobutton(root, text="Chậm", variable=self.delay_time, value=1)
        self.radio2 = tk.Radiobutton(root, text="Vừa", variable=self.delay_time, value=0.5)
        self.radio3 = tk.Radiobutton(root, text="Nhanh", variable=self.delay_time, value=0.2)

        self.radio1.pack(padx=5, pady=(5,0), anchor="w")
        self.radio2.pack(padx=5, pady=0, anchor="w")
        self.radio3.pack(padx=5, pady=0, anchor="w")

    def start_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--guest')

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('https://www.facebook.com/') 

        email_field = self.driver.find_element(By.NAME, 'email')
        password_field = self.driver.find_element(By.NAME, 'pass')

        email_field.send_keys('0932140098')
        password_field.send_keys('@Duchieu#')

        login_button = self.driver.find_element(By.NAME, 'login')
        login_button.click()

    def start_scrolling(self):
        if not self.is_scrolling:  
            self.is_scrolling = True
            self.scrolling_thread = threading.Thread(target=self.scroll)
            self.scrolling_thread.start()
    
    def scroll(self):
        print('---scroll---')
        self.is_scrolling = True
        while self.is_scrolling:
            try:
                elements = self.driver.find_elements(By.XPATH, "//div[@aria-label='Thêm bạn bè' and @role='button']")
                for invite_button in elements:
                    self.driver.execute_script("arguments[0].style.border='3px solid red'", invite_button)
                    # invite_button.click()
                
                pyautogui.scroll(-300)
                time.sleep(self.delay_time.get())

            except NoSuchElementException:
                print('NOT FOUND')
                time.sleep(1)
                continue

            except StaleElementReferenceException:
                print('STALE ELEMENT')
                time.sleep(1)
                continue

            except Exception as e:
                print('Error', e)

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
