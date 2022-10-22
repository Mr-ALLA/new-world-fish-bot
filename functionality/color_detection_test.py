import cv2
import numpy as np
import pyautogui
from time import sleep

color_discrepency = 4
def find_green(img):
    lower, upper = ( # GREEN
        [4 - color_discrepency, 227 - color_discrepency, 162 - color_discrepency],
        [4 + color_discrepency, 227 + color_discrepency, 162 + color_discrepency],
    )

    color_lower = np.array(lower)
    color_upper = np.array(upper)

    mask = cv2.inRange(img, color_lower, color_upper)
    if mask.any():
        print("WE GOT THE COLOR NIGGA!!")
        return True
    print("No color yet...")
    sleep(1)
    return False

while True:
    image = pyautogui.screenshot()
    img_arr = np.array(image)
    find_green(img_arr)
    print("Searching for the green color...")
    if find_green(img_arr) == True:
        print("WE FOUND THE COOOLOOOOOOOR")
        break
    sleep(1)


#colors:
  #green:
    #r: 4
    #g: 227
    #b: 162
  #brown:
    #r: 230
    #g: 110
    #b: 22
  #red:
    #r: 109
    #g: 18
    #b: 21


