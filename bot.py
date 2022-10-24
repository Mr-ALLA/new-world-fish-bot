import sys
sys.path.append('../NWFBot')
import functionality.fishing_actions as fl
from time import sleep

keep_going = True
while keep_going:
    result_from_model = fl.return_correct_action()
    if result_from_model == 0:
        print("Nothing happening. Will attempt to cast rod...")
        sleep(3)
        fl.casting()
    elif result_from_model == 2:
        print("Casting was successful!")
        fl.trying_to_catch()
    elif result_from_model == 3:
        print("Spotted green color! Initiating reeling...")
        fl.reeling()
    else:
        print("Image recognition model returned null! Something is wrong!")