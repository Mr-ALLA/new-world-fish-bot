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

antiafk_start = datetime.now()
repair_start = datetime.now()
antiafk_threshold_seconds = 1000 #Around 17 minutes
repair_threshold = int 
time_since_antiafk = datetime.now()
time_since_repair = datetime.now()
is_bait_active = int
bait_slot = int
fish_caught = 0

def get_repair_threshold():
    global repair_threshold
    return repair_threshold

def set_repair_threshold(x):
    global repair_threshold
    repair_threshold = x

def get_bait_active():
    global is_bait_active
    return is_bait_active

def set_bait_active(x):
    global is_bait_active
    is_bait_active = x

def get_bait_slot():
    global bait_slot
    return bait_slot

def set_bait_slot(x):
    global bait_slot
    bait_slot = x

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
    global antiafk_start
    global repair_start
    global time_since_repair
    debug("Time since last Anti-AFK: " + str(time_since_antiafk))
    debug("Time since last repair: " + str(time_since_repair))
    info("Pausing in case of rare catch inspect animation...")
    sleep(random.uniform(5.4,5.8))
    pyautogui.keyUp('b')
    time_since_antiafk = datetime.now() - antiafk_start
    if time_since_antiafk.total_seconds() > antiafk_threshold_seconds:
        info("Moving to avoid getting kicked for idling...")
        sleep(1)
        anti_afk()
    time_since_repair = datetime.now() - repair_start
    if time_since_repair.total_seconds() > get_repair_threshold():
        info("Time to repair the fishing rod...")
        sleep(1)
        repair_rod()
    sleep(1)
    info("Trying to cast fishing rod...")
    cast_time = random.uniform(1.5,2.0)
    debug("Casting the rod for a duration of: " + str(round(cast_time,2)) + " seconds!")
    mouseclick_delay(cast_time)
    sleep(0.5)
    info("Successful cast!")
    pyautogui.keyDown('b')
    sleep(2)

def trying_to_catch():
    start_time = datetime.now()
    info("Waiting for a fish to bite...")
    while True:
        time_delta = datetime.now() - start_time
        if time_delta.total_seconds() >= 25:
            info("Catching timed out! No bites. Trying again...")
            break
        if ir.image_recog_caught() == 1:
            pyautogui.click()
            info("Caught one!")
            sleep(1)
            break

def reeling():
    global fish_caught
    info("Reeling a fish...")
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
            fish_caught = fish_caught + 1
            info("Fish caught! The bot has caught: " + str(fish_caught) + " fish!")
            break

def mouseclick_delay(delay):
    pyautogui.mouseDown()
    sleep(delay)
    pyautogui.mouseUp()

def anti_afk():
    global antiafk_start
    move_time = random.uniform(0.4,0.8)
    anti_afk_movement(move_time)
    antiafk_start = datetime.now()
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

def repair_rod():
    global repair_start
    screen_res = pyautogui.size()
    arm_disarm_rod()
    sleep(1)
    pyautogui.press('tab')
    repair_start = datetime.now()
    sleep(1)
    if screen_res[1] == 1440:
        pyautogui.click(1152,663)
        sleep(1)
        pyautogui.keyDown('r')
        sleep(0.8)
        pyautogui.click(1152,663)
        sleep(0.8)
        pyautogui.keyUp('r')
        sleep(0.8)
        pyautogui.press('e')
        sleep(0.8)
        pyautogui.press('tab')
        sleep(0.8)
        pyautogui.press('f3')
        info("Repairing complete! Resuming fishing...")
        sleep(1)
    elif screen_res[1] == 1080:
        pyautogui.click(864,497)
        sleep(1)
        pyautogui.keyDown('r')
        sleep(0.8)
        pyautogui.click(864,497)
        sleep(0.8)
        pyautogui.keyUp('r')
        sleep(0.8)
        pyautogui.press('e')
        sleep(0.8)
        pyautogui.press('tab')
        sleep(0.8)
        pyautogui.press('f3')
        info("Repairing complete! Resuming fishing...")
        sleep(1)
    else:
        info("Repair failed due to unsupported screen resolution. Auto-repair only works with 1080p or 1440p monitors.")

def equip_bait():
    screen_res = pyautogui.size()
    info("Equipping bait...")
    arm_disarm_rod()
    sleep(3)
    pyautogui.press('r')
    sleep(1)
    if screen_res[1] == 1440:
        if get_bait_slot() == 1:
            pyautogui.click(1588,627)
            sleep(3)
            pyautogui.click(1995,1097)
            sleep(0.4)
            pyautogui.click()
            sleep(2)
        elif get_bait_slot() == 2:
            pyautogui.click(1711,623)
            sleep(3)
            pyautogui.click(1995,1097)
            sleep(0.4)
            pyautogui.click()
            sleep(2)
        elif get_bait_slot() == 3:
            pyautogui.click(1814,619)
            sleep(3)
            pyautogui.click(1995,1097)
            sleep(0.4)
            pyautogui.click()
            sleep(2)
        else:
            info("BAIT EQUIP FAILED. No bait slot was chosen in the settings. Restart the program and remember to choose a bait slot.")
    elif screen_res[1] == 1080:
        if get_bait_slot() == 1:
            pyautogui.click(1191,470)
            sleep(3)
            pyautogui.click(1496,823)
            sleep(0.4)
            pyautogui.click()
            sleep(2)
        elif get_bait_slot() == 2:
            pyautogui.click(1283,467)
            sleep(3)
            pyautogui.click(1496,823)
            sleep(0.4)
            pyautogui.click()
            sleep(2)
        elif get_bait_slot() == 3:
            pyautogui.click(1360,464)
            sleep(3)
            pyautogui.click(1496,823)
            sleep(0.4)
            pyautogui.click()
            sleep(2)
        else:
            info("BAIT EQUIP FAILED. No bait slot was chosen in the settings. Restart the program and remember to choose a bait slot.")
    else:
        info("BAIT EQUIP FAILED. Unsupported screen resolution! Only 1920x1080 and 2560x1440 monitors supported!")


def arm_disarm_rod():
    pyautogui.press('f3')
    sleep(1.8)
    pyautogui.press('f3')

def image_reg_broken():
    info("Image recognition model returned NULL! Something is very wrong!")