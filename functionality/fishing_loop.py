from functionality import image_recognition as ir
from functionality import color_detection as cd


keep_going = True
while keep_going:
    result_from_model = ir.return_correct_action()
    if result_from_model == 0:
        print("Nothing happening... Attempting to cast rod.")
        ir.casting()
    ##elif result_from_model == 1:
        ##print("Wrong Place!!") #handled in the trying to catch function
    elif result_from_model == 2:
        ir.trying_to_catch()
    elif result_from_model == 3:
        print("Model saw the red reel color!!")
        ir.reeling()
    else:
        print("Something is wrong with the model!!")