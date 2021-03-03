import cv2
import time
import numpy as np
import pyscreenshot as ImageGrab
import pyautogui
from PIL import ImageGrab
template = cv2.imread('Screenshot_2.png', 0)
x = 1
while True:
    x = x + 1
    w, h = template.shape[::-1]
#filename1 = 'Dreehanit.png'

    base_screen = ImageGrab.grab(bbox=(1150, 0, 1900, 250))
#cv2.imwrite(filename1, base_screen)

    base_screen.save('Dreehanit.png')

    img_rgb = cv2.imread('Dreehanit.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= 0.7)
    print(len(loc))
    for i in loc:
        print(i)

    try:
        if loc[0] != None and loc[1] != None:
            print('Fuck Yeaahhh Babe!!!!')
            pyautogui.press('3', presses= 5, interval=0.0)
            #time.sleep(0.1)
            #pyautogui.press("3")
        else:
            pass
    except:
        pass


    print('--------------------------------------------------')