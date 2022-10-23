import image_recognition as ir
import color_detection as cd
from time import sleep


keep_going = True
while keep_going:
    result_from_model = ir.return_correct_action()
    if result_from_model == 0:
        print("Nothing happening. Will attempt to cast rod...")
        sleep(3)
        ir.casting()
    elif result_from_model == 2:
        print("Casting was successful!")
        ir.trying_to_catch()
    elif result_from_model == 3:
        print("Spotted green color! Initiating reeling...")
        ir.reeling()
    else:
        print("Image recognition model returned null! Something is wrong!")