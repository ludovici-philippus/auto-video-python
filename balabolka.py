import pyautogui
import keyboard
from time import sleep

class Balabolka(object):
    def __init__(self):
        pyautogui.PAUSE = 0.5
        sleep(2)
        self.main()
        #self.get_mouse_pos()
    
    def numbers_remover(self):
        pyautogui.hotkey("ctrl", "r")
        for number in range(0, 10):
            pyautogui.press(str(number))
            pyautogui.moveTo(1197, 556)
            pyautogui.click()
            pyautogui.moveTo(859, 504)
            pyautogui.doubleClick()
    def main(self):
        self.numbers_remover()
    
    def get_mouse_pos(self):
        pyautogui.mouseInfo()

if __name__ != "__main__.py":
    balabolka = Balabolka()