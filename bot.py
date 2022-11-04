import sys
sys.path.append('../NWFBot')
import functionality.fishing_actions as fa
from wrappers.logging_wrapper import debug
from time import sleep

keep_going = bool
def set_keep_going(x):
    global keep_going
    keep_going = x

def get_keep_going():
    global keep_going
    return keep_going

def start_fishing():
    global keep_going
    debug("YOUR SETTINGS ARE: REPAIR: " + str(fa.get_repair_threshold()) + ". IS BAIT ACTIVE?: " + str(fa.get_bait_active()) + ". WHAT BAIT SLOT?: " + str(fa.get_bait_slot()))
    if fa.get_bait_active() == 1:
        fa.equip_bait()
        sleep(1)
    while True:
        while keep_going == True:
            result_from_model = fa.return_correct_action()
            if result_from_model == 0:
                fa.casting()
            elif result_from_model == 2:
                fa.trying_to_catch()
            elif result_from_model == 3:
                fa.reeling()
            else:
                fa.image_reg_broken()
        sleep(0.3)