import sys
sys.path.append('../NWFBot')
import tkinter.messagebox
from tkinter import *
from functionality.bot import start_fishing,set_keep_going
import threading
from wrappers.logging_wrapper import info
from functionality.fishing_actions import set_repair_threshold,set_bait_active,set_bait_slot
from time import sleep

nw_version = 1.2

def load_gui():
    win=Tk() #creating the main window and storing the window object in 'win'
    win.title('funny ocean creature catching helper v' + str(nw_version)) #setting title of the window
    win.geometry('600x250') #setting the size of the window
    win.resizable(width=False, height=False)
    win.bind_all("<Button-1>", lambda event: event.widget.focus_set())

    can=Canvas(win, width=600, height=250)   
    #rect1=can.create_rectangle(590, 25, 400, 65, fill="black")
    #rect2=can.create_rectangle(300, 10, 200, 200, fill="black")
    seperator1=can.create_rectangle(154,0,156,250, fill="black")
    seperator2=can.create_rectangle(368,0,370,205, fill="black")
    can.pack()
    
    # Start button
    def start_func():
        set_keep_going(True)
        replace_button(win)
        get_repair_value()
        is_bait_active()
        bait_slot()
        info("STARTING BOT... Please make sure the game window is in focus within the next 5 seconds...")
        sleep(5)
        t2.start()
    start_btn=Button(win,text="Start Fishing", width=12,height=2,command=start_func,bg="green")
    start_btn.place(x=30,y=15)

    # Stop button
    def stop_func():
        set_keep_going(False)
        info("PAUSING BOT AFTER CURRENT FISHING LOOP...")
    stop_btn=Button(win,text="Pause Fishing", width=12,height=2,command=stop_func,bg="red")
    stop_btn.place(x=30,y=70)

    # Choose repair time column
    def get_repair_value():
        value = float(ent1.get())
        set_repair_threshold(value)
    Label(win, text='Repair Frequency',font='Roboto 12 bold').place(x=415, y=3)
    Label(win, text='Repair Fishing Rod Every:').place(x=417, y=37)
    Label(win, text='seconds').place(x=528, y=72)
    Label(win, text='Default: 1800 seconds (~30 minutes)').place(x=388, y=112)
    ent1 = Entry(win)  
    ent1.place(x=398, y=75)
    ent1.insert(1800,"1800") # have to check whether or not this actually gets overridden by user input
    rod_icon = PhotoImage(file='resources/rod_icon.png')
    Label(win,image=rod_icon).place(x=450,y=140)
    bait_icon = PhotoImage(file='resources/bait_icon.png')
    Label(win,image=bait_icon).place(x=225,y=140)

    # Bait column
    def is_bait_active():
        value = bait_active.get()
        set_bait_active(value)
    bait_active = IntVar()
    cb1=Checkbutton(win, text='Auto Bait Select Active', variable=bait_active, onvalue=1, offvalue=0, height=0, width=18)
    cb1.place(x=185,y=35)
    def bait_slot():
        value = bait_slot_var.get()
        set_bait_slot(value)
    bait_slot_var = IntVar()
    rb1=Radiobutton(win, text='Bait Slot 1', variable=bait_slot_var, value=1)
    rb2=Radiobutton(win, text='Bait Slot 2', variable=bait_slot_var, value=2)
    rb3=Radiobutton(win, text='Bait Slot 3', variable=bait_slot_var, value=3)
    rb1.place(x=205,y=60)
    rb2.place(x=205,y=85)
    rb3.place(x=205,y=110)
    Label(win, text='Auto Bait Selection',font='Roboto 12 bold').place(x=190, y=3)

    # Tutorial
    Label(win,bg="gold",
    text='When youre ready to fish, \n press start fishing and \n make sure the game \n window is in focus. \n The bot will then catch \n fish on its own.').place(x=5, y=130) 

    # Settings warning
    Label(win,bg="gold",
    text='Please keep in mind that the settings cannot be changed after starting the bot. \n Youll have to restart the program entirely to change settings again.').place(x=167, y=210)

    win.mainloop() #running the loop that works as a trigger

t1 = threading.Thread(target=load_gui)
t2 = threading.Thread(target=start_fishing)
t1.start()


def replace_button(obj):
    def resume_func():
        set_keep_going(True)
        info("RESUMING FISHING...")
    resume_btn=Button(obj,text="Resume Fishing", width=12,height=2,command=resume_func,bg="yellow")
    resume_btn.place(x=30,y=15)
