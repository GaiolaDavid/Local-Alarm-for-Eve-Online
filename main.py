# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
import playsound
import threading
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from PIL import ImageGrab
from functools import partial
from screeninfo import *

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)
ImageGrab.grab()
running = True
windowpos = [100, 100, 100, 100]
root = tk.Tk()

topleft = 0
for m in get_monitors():
    if (topleft > m.x): topleft = m.x


def opennewwindow():
    app1 = App1(Tk())


class App:
    def __init__(self, root):
        # setting title
        root.title("Local Alarm")
        # setting window size
        width = 386
        height = 396
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_670 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_670["font"] = ft
        GLabel_670["fg"] = "#333333"
        GLabel_670["justify"] = "center"
        GLabel_670["text"] = "Made by Dr0ppy#5966"
        GLabel_670.place(x=80, y=20, width=203, height=35)

        GButton_367 = tk.Button(root)
        GButton_367["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_367["font"] = ft
        GButton_367["fg"] = "#000000"
        GButton_367["justify"] = "center"
        GButton_367["text"] = "Chatbox Position Helper"
        GButton_367.place(x=90, y=110, width=180, height=33)
        GButton_367["command"] = self.GButton_367_command

        GButton_822 = tk.Button(root)
        GButton_822["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_822["font"] = ft
        GButton_822["fg"] = "#000000"
        GButton_822["justify"] = "center"
        GButton_822["text"] = "Load from file"
        GButton_822.place(x=130, y=170, width=110, height=30)
        GButton_822["command"] = self.GButton_822_command

        GLabel_750 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_750["font"] = ft
        GLabel_750["fg"] = "#333333"
        GLabel_750["justify"] = "center"
        GLabel_750["text"] = "Close window to start"
        GLabel_750.place(x=75, y=60, width=209, height=44)

    def GButton_367_command(self):
        opennewwindow()

    def GButton_822_command(self):
        file = open('Position.txt', 'r')
        string = file.read()
        stringsplit = string.split(' ')
        windowpos[0] = int(stringsplit[0])
        windowpos[1] = int(stringsplit[1])
        windowpos[2] = int(stringsplit[2])
        windowpos[3] = int(stringsplit[3])
        file.close()
        print(windowpos)


class App1:
    def __init__(self, root):
        # setting title
        root.title("Local Alarm Visual Indicator")
        # setting window size
        width = 164
        height = 171
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)
        GButton_757 = tk.Button(root)
        GButton_757["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_757["font"] = ft
        GButton_757["fg"] = "#000000"
        GButton_757["justify"] = "center"
        GButton_757["text"] = "Pick Location"
        GButton_757.place(x=40, y=10, width=180, height=50)
        GButton_757["command"] = self.GButton_757_command

    def GButton_757_command(self):
        box = pyautogui.getWindowsWithTitle("Local Alarm Visual Indicator")
        print(box[0])
        windowpos[0], windowpos[1], windowpos[2], windowpos[3] = box[0].box
        windowpos[0] = windowpos[0] - topleft
        print(windowpos)
        file = open('Position.txt', 'w')
        string = str(windowpos)
        string = string.replace(',', '')
        string = string.replace('[', '')
        string = string.replace(']', '')
        file.write(string)
        file.close()


if __name__ == '__main__':

    app = App(root)
    root.mainloop()
    print("Running")
    soundFile = './Cylen.wav'
    while running:
        happens = False
        test = pyautogui.locateOnScreen('1.png', region=(windowpos[0], windowpos[1], windowpos[2], windowpos[3]),
                                        confidence = 0.9)
        if str(test) != "None":
            happens = True
        #print(test)
        #print(happens)
        test = pyautogui.locateOnScreen('2.png', region=(windowpos[0], windowpos[1], windowpos[2], windowpos[3]),
                                        confidence = 0.9)
        if str(test) != "None":
            happens = True
        #print(test)
        #print(happens)
        test = pyautogui.locateOnScreen('3.png', region=(windowpos[0], windowpos[1], windowpos[2], windowpos[3]),
                                        confidence = 0.9)
        if str(test) != "None":
            happens = True
        #print(test)
        #print(happens)
        if happens:
            playsound.playsound(soundFile)
        else:
            pyautogui.sleep(1)
        #print(happens)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
