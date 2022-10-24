import sys
sys.path.append('../NWFBot')
from python_imagesearch.imagesearch import imagesearch
import pyautogui
import numpy as np
from time import sleep
from datetime import datetime
import random
import functionality.color_detection as cd
from wrappers.logging_wrapper import debug, info
import functionality.image_recognition as ir

program_start = datetime.now()
antiafk_threshold_seconds = 1000 #Around 17 minutes
time_since_antiafk = datetime.now()

def return_correct_action():
    image = pyautogui.screenshot()
    img_arr = np.array(image)
    if ir.image_recog_waiting() == 1:
        return 2
    elif cd.find_green(img_arr) == True:
        return 3
    else:
        return 0

def casting():
    global time_since_antiafk
    global program_start
    info("Idling... Will attempt to cast rod.")
    sleep(1)
    time_since_antiafk = datetime.now() - program_start
    if time_since_antiafk.total_seconds() > antiafk_threshold_seconds:
        info("Moving to avoid getting kicked for idling...")
        sleep(1)
        anti_afk() 
    debug("Time Since last Anti AFK: " + str(time_since_antiafk))
    info("Pausing for 5s in case of fish inspect animation...")
    sleep(5)
    pyautogui.keyUp('b')
    info("Casting Fishing Rod!")
    cast_time = random.uniform(1.2,2.2)
    debug("Casting the rod for a duration of: " + str(round(cast_time,2)) + " seconds!") #trying to round during the print..
    mouseclick_delay(cast_time)
    sleep(0.5)
    info("Successful cast!")
    pyautogui.keyDown('b') # To counteract the permanent movement of the camera after inspecting a caught fish
    sleep(1)

def trying_to_catch():
    start_time = datetime.now()
    info("Waiting for a fish to bite...")
    while True:
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 25:
            info("Catching timed out! No bites...")
            break
        if ir.image_recog_caught() == 1:
            pyautogui.click()
            info("Fish on the line!")
            sleep(1)
            break

def reeling():
    info("Reeling...")
    while True:
        default_pause = random.uniform(0.2,0.3)
        orange_pause = random.uniform(1.0,1.4)
        red_pause = random.uniform(2.0,2.5)
        reel_dur_green = random.uniform(0.4,0.8)
        reel_dur_orange = random.uniform(0.3,0.5)

        image = pyautogui.screenshot()
        img_arr = np.array(image)

        if cd.find_green(img_arr) == True:
            debug("Spotted green color! Reeling...")
            mouseclick_delay(reel_dur_green)
            sleep(default_pause)
        
        elif cd.find_orange(img_arr) == True:
            debug("Spotted orange color! Pausing for a moment...")
            sleep(orange_pause)
            debug("Resuming reel...")
            mouseclick_delay(reel_dur_orange)
            sleep(default_pause)

        elif cd.find_red(img_arr) == True:
            debug("Spotted red color! Better pause for a while...")
            sleep(red_pause)

        else:
            info("Fish caught/Line broken! Stopping reel...")
            break

def mouseclick_delay(delay):
    pyautogui.mouseDown()
    sleep(delay)
    pyautogui.mouseUp()

def anti_afk():
    global program_start
    move_time = random.uniform(0.4,0.8)
    anti_afk_movement(move_time)
    program_start = datetime.now()
    debug("Anti-AFK complete! Resuming fishing...")
    sleep(1)

def anti_afk_movement(time):
    half_chance = random.randint(0,1)
    pyautogui.press('f3')
    sleep(1)
    if half_chance == 1:
        pyautogui.keyDown('w')
        sleep(time/1.8)
        pyautogui.keyUp('w')
        sleep(1)
        pyautogui.keyDown('s')
        sleep(time)
        pyautogui.keyUp('s')
        sleep(1)
        pyautogui.press('f3')
    else:
        pyautogui.keyDown('d')
        sleep(time)
        pyautogui.keyUp('d')
        sleep(1)
        pyautogui.keyDown('a')
        sleep(time)
        pyautogui.keyUp('a')
        sleep(1)
        pyautogui.press('f3')

def image_reg_broken():
    info("Image recognition model returned NULL! Something is very wrong!")