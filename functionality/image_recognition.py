from python_imagesearch.imagesearch import imagesearch
import pyautogui
import numpy as np
from time import sleep
from datetime import datetime
import random
import color_detection as cd


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

def check_reel():
    stop_reel = imagesearch("./resources/stop_reeling.png")
    if stop_reel[0] != -1:
        return 1
    else:
        return 0

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
            print("Clicking to catch!")
            sleep(1.5)
            break

def casting():
    print("Pausing in case of fish inspect animation...")
    sleep(6)
    pyautogui.keyUp('b')
    print("Casting Fishing Rod!")
    cast_time = random.uniform(1.5,2.2)
    round(cast_time, 2)
    print("Casting the rod for a duration of: " + str(cast_time) + " seconds!")
    mouseclick_delay(cast_time)
    sleep(0.5)
    pyautogui.keyDown('b') # To counteract the permanent movement of the camera after inspecting a caught fish
    sleep(2)

def reeling():
    while True:
        default_pause = random.uniform(0.4,0.8)
        orange_pause = random.uniform(1.0,1.8)
        red_pause = random.uniform(2.0,2.5)
        reel_dur_green = random.uniform(1.6,2.0)
        reel_dur_orange = random.uniform(1.0,1.4)

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


#keep_going = True
#while keep_going:
    #result_from_model = return_correct_action()
    #if result_from_model == 0:
        #print("Nothing happening... Attempting to cast rod.")
        #casting()
    ##elif result_from_model == 1:
        ##print("Wrong Place!!") #handled in the trying to catch function
    #elif result_from_model == 2:
        #trying_to_catch()
    #elif result_from_model == 3:
        #print("Model saw the red reel color!!")
        #reeling()
    #else:
        #print("Something is wrong with the model!!")

