import image_recognition as ir
import color_detection as cd
from time import sleep


keep_going = True
while keep_going:
    result_from_model = ir.return_correct_action()
    if result_from_model == 0:
        print("Main Loop: Nothing happening... Attempting to cast rod.")
        print("Main Loop: Attemtping to cast in 5 seconds...")
        sleep(5)
        ir.casting()
    elif result_from_model == 2:
        print("Main Loop: Spotted waiting for fish. Going to trying to catch...")
        ir.trying_to_catch()
    elif result_from_model == 3:
        print("Main Loop: Green color spotted, reeling time!!")
        ir.reeling()
    else:
        print("Main Loop: Something is wrong with the model!!")