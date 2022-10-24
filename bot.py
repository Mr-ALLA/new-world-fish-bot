import sys
sys.path.append('../NWFBot')
import functionality.fishing_actions as fl
from wrappers.logging_wrapper import debug, info
from time import sleep

keep_going = True
while keep_going:
    result_from_model = fl.return_correct_action()
    if result_from_model == 0:
        info("Idling... Will attempt to cast rod.")
        sleep(3)
        fl.casting()
    elif result_from_model == 2:
        info("Successful cast!")
        fl.trying_to_catch()
    elif result_from_model == 3:
        debug("Spotted green color! Initiating reeling...")
        fl.reeling()
    else:
        info("Image recognition model returned NULL! Something is very wrong!")