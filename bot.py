import sys
sys.path.append('../NWFBot')
import functionality.fishing_actions as fa

keep_going = True
while keep_going:
    result_from_model = fa.return_correct_action()
    if result_from_model == 0:
        fa.casting()
    elif result_from_model == 2:
        fa.trying_to_catch()
    elif result_from_model == 3:
        fa.reeling()
    else:
        fa.image_reg_broken()