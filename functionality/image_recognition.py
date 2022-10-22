from python_imagesearch.imagesearch import imagesearch
import pyautogui
from time import sleep
from datetime import datetime



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
    stop_reel = imagesearch("./resources/waiting_for_fish.png")
    if stop_reel[0] != -1:
        return 1
    else:
        return 0

def trying_to_catch():
    start_time = datetime.now()
    print(start_time)
    stop_catching = False
    while stop_catching == False:
        time_delta = datetime.now() - start_time
        print(time_delta)
        if time_delta.total_seconds() >= 25:
            print("Catching timeout!")
            break
        fish_found = imagesearch("./resources/fish_caught.png")
        if fish_found[0] != -1:
            pyautogui.click()
            print("Clicking to catch!")
        print("Waiting for fish...")


def return_correct_action():
    fish_found = imagesearch("./resources/fish_caught.png")
    waiting_for_fish = imagesearch("./resources/waiting_for_fish.png")
    if fish_found[0] != -1:
        return 1
    elif waiting_for_fish[0] != -1:
        return 2
    else:
        return 0


keep_going = True
while keep_going:
    result_from_model = return_correct_action()
    if result_from_model == 0:
        print("Nothing happening")
    elif result_from_model == 1:
        print("Wrong Place!!")
    elif result_from_model == 2:
        print("Model is waiting for a fish!!")
        trying_to_catch()
    elif result_from_model == 3:
        print("Model saw the red reel color!!")
    else:
        print("Something is wrong with the model!!")

