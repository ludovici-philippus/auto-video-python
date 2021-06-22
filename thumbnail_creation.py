from tkinter.constants import RIGHT
import pyautogui
from time import sleep
import image_download
from os import system
from pyperclip import copy
from threading import Thread

class Thumbnail:
    def __init__(self, text_top, text_bottom=""):
        #self.image = image_download.ImageDownloader(input("Enter the image's name: "))
        pyautogui.PAUSE = 0.5
        self.video_name = "ADMIRÁVEL MUNDO NOVO - ALDOUS HUXLEY (AUDIOLIVRO AUDIOBOOK)"
        self.text_top = text_top.upper()
        self.text_bottom = text_bottom.upper()
        self.font = "Burbank Big Condensed, Semi-Bold"
        self.font_size = 150
        #self.main()
        sleep(2)
        self.get_mouse()

    def open_gimp(self):
        # Abrir o gimp
        system(r'gimp "/home/luis/Backup/Backup windows/Audiolivros template 2.xcf"')
        
    def put_the_image(self):
        # To avoid layer's bugs
        pyautogui.moveTo(1809, 657)
        pyautogui.click()

        pyautogui.hotkey("ctrl", "alt", "o")
        pyautogui.moveTo(502, 401)
        pyautogui.click()
        pyautogui.press("right")
        pyautogui.press("down")
        pyautogui.press("enter")
        sleep(4)
    
    def resize_image(self):
        pyautogui.hotkey("ctrl", "alt", "r")
        pyautogui.write("1280")
        pyautogui.moveTo(1094, 687)
        pyautogui.click()
    
    def improve_saturation(self):
        self.click_in_the_layer()
        pyautogui.press("s")
        pyautogui.moveTo(1009, 503)
        pyautogui.click()
        pyautogui.moveTo(1011, 530)
        pyautogui.click()
        pyautogui.moveTo(1044, 655)
        pyautogui.click()

    def improve_curves(self):
        self.click_in_the_layer()
        pyautogui.press("c")
        pyautogui.moveTo(323, 378)
        pyautogui.click()
        pyautogui.press("enter")

    def edit_text(self):
        pyautogui.press("t")
        pyautogui.moveTo(412, 484)
        pyautogui.click()
        pyautogui.moveTo(402, 585)
        pyautogui.click()

        # Write new text
        pyautogui.hotkey("ctrl", "a")
        copy(self.text_top)
        pyautogui.hotkey("ctrl", 'v')
        pyautogui.press("esc")
        pyautogui.hotkey("shift", "t")
        pyautogui.moveTo(412, 484)
        pyautogui.mouseDown()
        pyautogui.moveTo(450, 514)
        pyautogui.mouseUp()
        pyautogui.press("enter")
        self.adjust_the_text(411, 429)
        self.add_shadow()

        if self.text_bottom != "":
            self.click_in_the_layer()
            pyautogui.press("t")
            pyautogui.moveTo(332, 628)
            pyautogui.click()
            copy(self.text_bottom)
            pyautogui.hotkey("ctrl", "v")
            
            pyautogui.hotkey("ctrl", "a")
            pyautogui.moveTo(397, 571)
            pyautogui.click()
            pyautogui.hotkey("ctrl", "a")
            pyautogui.write(self.font)

            pyautogui.moveTo(545, 571)
            pyautogui.click()
            pyautogui.hotkey("ctrl", "a")
            pyautogui.write(str(self.font_size))

            pyautogui.moveTo(627, 600)
            pyautogui.click()
            pyautogui.moveTo(754, 680)
            pyautogui.doubleClick()
            pyautogui.write("ffffff")
            pyautogui.moveTo(688, 779)
            pyautogui.click()
            pyautogui.press('esc')
            pyautogui.press('esc')

            pyautogui.moveTo(402, 704)
            pyautogui.hotkey("shift", "t")
            pyautogui.mouseDown()
            pyautogui.moveTo(402, 599)
            pyautogui.mouseUp()
            pyautogui.press("enter")
            self.add_shadow()

    def adjust_the_text(self, x, y):
        # Faz um degrade no texto
        pyautogui.hotkey("shift", "o")
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.press("g")
        pyautogui.moveTo(x-20, y-60)
        pyautogui.mouseDown()
        
        pyautogui.moveTo(x+200, y+80)
        pyautogui.mouseUp()
        pyautogui.press("enter")
        
        # Reseta a seleção
        pyautogui.press("r")
        pyautogui.moveTo(967, 988)
        pyautogui.click()

    def add_shadow(self):
        # Adiciona sombra no texto        
        pyautogui.hotkey("ctrl", "alt", "s")
        pyautogui.moveTo(991, 502)
        pyautogui.doubleClick()
        #pyautogui.moveTo(1028, 531)
        #pyautogui.click()
        pyautogui.moveTo(1042, 811)
        pyautogui.click()

    def export_thumb(self):
        pyautogui.hotkey("ctrl", "shift", "e")
        copy(self.video_name)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        sleep(3)
        pyautogui.press("enter")

    def get_mouse(self):
        pyautogui.mouseInfo()

    def click_in_the_layer(self):
        pyautogui.moveTo(1799, 659)
        pyautogui.click()
    
    def main(self):
        Thread(target=self.open_gimp).start()
        sleep(5)
        self.put_the_image()    
        self.resize_image()
        self.improve_saturation()
        self.improve_curves()
        self.edit_text()
        self.export_thumb()

thumb = Thumbnail("ADMIRÁVEL", "MUNDO NOVO")


