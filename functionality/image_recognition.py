from python_imagesearch.imagesearch import imagesearch
import pyautogui
import numpy as np
from time import sleep
from datetime import datetime
import random
import color_detection as cd
import sys
from wrappers.logging_wrapper import debug, info
sys.path.append('../NWFBot')

def check_for_fish():
    fish_found = imagesearch("./resources/fish_caught.png")
    if fish_found[0] != -1:
        return 1
    else:
        return 0


def check_if_waiting():
    waiting_for_fish = imagesearch("./resources/waiting_for_fish.png")
    if waiting_for_fish[0] != -1:
        return 1
    else:
        return 0

program_start = datetime.now()
antiafk_threshold_seconds = 1000 #Around 17 minutes
time_since_antiafk = datetime.now()

def mouseclick_delay(delay):
    pyautogui.mouseDown()
    sleep(delay)
    pyautogui.mouseUp()

def trying_to_catch():
    start_time = datetime.now()
    print("Waiting for a fish to bite...")
    while True:
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 25:
            print("Catching timed out! No bites...")
            break
        fish_found = imagesearch("./resources/fish_caught.png")
        if fish_found[0] != -1:
            pyautogui.click()
            print("Fish on the line!")
            sleep(1)
            break

def casting():
    global time_since_antiafk
    global program_start
    time_since_antiafk = datetime.now() - program_start
    if time_since_antiafk.total_seconds() > antiafk_threshold_seconds:
        print("Running Anti-AFK to avoid getting kicked...")
        sleep(1)
        anti_afk() 
    print("Time Since Anti AFK: " + str(time_since_antiafk))
    print("Pausing in case of fish inspect animation...")
    sleep(6)
    pyautogui.keyUp('b')
    print("Casting Fishing Rod!")
    cast_time = random.uniform(1.5,2.2)
    print("Casting the rod for a duration of: " + str(round(cast_time,2)) + " seconds!") #trying to round during the print..
    mouseclick_delay(cast_time)
    sleep(0.5)
    pyautogui.keyDown('b') # To counteract the permanent movement of the camera after inspecting a caught fish
    sleep(1)

def reeling():
    while True:
        default_pause = random.uniform(0.2,0.3)
        orange_pause = random.uniform(1.0,1.4)
        red_pause = random.uniform(2.0,2.5)
        reel_dur_green = random.uniform(0.6,1.0)
        reel_dur_orange = random.uniform(0.4,0.6)

        image = pyautogui.screenshot()
        img_arr = np.array(image)

        if cd.find_green(img_arr) == True:
            print("Spotted green color! Reeling...")
            mouseclick_delay(reel_dur_green)
            sleep(default_pause)
        
        elif cd.find_orange(img_arr) == True:
            print("Spotted orange color! Pausing for a moment...")
            sleep(orange_pause)
            print("Resuming reel...")
            mouseclick_delay(reel_dur_orange)
            sleep(default_pause)

        elif cd.find_red(img_arr) == True:
            print("Spotted red color! Better pause for a while...")
            sleep(red_pause)

        else:
            print("Fish caught/Line broken! Stopping reel...")
            break


def return_correct_action():
    waiting_for_fish = imagesearch("./resources/waiting_for_fish.png")
    image = pyautogui.screenshot()
    img_arr = np.array(image)
    if waiting_for_fish[0] != -1:
        return 2
    elif cd.find_green(img_arr) == True:
        return 3
    else:
        return 0


def anti_afk():
    global program_start
    move_time = random.uniform(0.4,0.8)
    anti_afk_movement(move_time)
    program_start = datetime.now()
    print("Anti-AFK complete! Resuming fishing...")
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

