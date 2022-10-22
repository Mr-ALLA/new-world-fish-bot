import cv2
import numpy as np
import pyautogui
from time import sleep

color_discrepency = 4 # The amount of discrepency the color can have to still be accepted. 4 is performing well.

def find_green(img):
  lower, upper = ( # GREEN
    [4 - color_discrepency, 227 - color_discrepency, 162 - color_discrepency],
    [4 + color_discrepency, 227 + color_discrepency, 162 + color_discrepency],
  )

  color_lower = np.array(lower)
  color_upper = np.array(upper)

  mask = cv2.inRange(img, color_lower, color_upper)
  if mask.any():
      return True
  return False

def find_orange(img):
  lower, upper = ( # ORANGE
    [230 - color_discrepency, 110 - color_discrepency, 22 - color_discrepency],
    [230 + color_discrepency, 110 + color_discrepency, 22 + color_discrepency],
  )

  color_lower = np.array(lower)
  color_upper = np.array(upper)

  mask = cv2.inRange(img, color_lower, color_upper)
  if mask.any():
    return True
  return False

def find_red(img):
  lower, upper = ( # RED
    [109 - color_discrepency, 18 - color_discrepency, 21 - color_discrepency],
    [109 + color_discrepency, 18 + color_discrepency, 21 + color_discrepency],
  )

  color_lower = np.array(lower)
  color_upper = np.array(upper)

  mask = cv2.inRange(img, color_lower, color_upper)
  if mask.any():
    return True
  return False
  


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


