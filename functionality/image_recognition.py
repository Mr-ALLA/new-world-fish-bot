import sys
sys.path.append('../NWFBot')
from python_imagesearch.imagesearch import imagesearch

def image_recog_result(img):
    if img[0] != -1:
        return 1
    else:
        return 0

def image_recog_caught():
    fish_caught = imagesearch("./resources/fish_caught.png")
    return image_recog_result(fish_caught)
    

def image_recog_waiting():
    waiting_for_fish = imagesearch("./resources/waiting_for_fish.png")
    return image_recog_result(waiting_for_fish)