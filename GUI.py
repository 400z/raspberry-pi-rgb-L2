from tkinter import * 
from tkinter.ttk import *
from gpiozero import RGBLED
import time
led = RGBLED(15,14,18)


led.off()
proceed = input("do you wish to proceed")

if proceed is not "y":
    print("this program won't continue")
else:
    
    led.color = (0,1,0)

    root = Tk() 

    def hello():
        print("hello")
        led.color = (0,0,0)
        led.color = (0.7,0.2,0)
        time.sleep(1)
        led.color = (1,0,0)
        time.sleep(2)
        led.color = (0.7,0.2,0)
        time.sleep(1)
        led.color = (0,1,0)

    Label(root, text = 'road safetty', font =( 'Verdana', 15)).pack(side = TOP, pady = 10) 
    photo =  PhotoImage(file = "/home/pi/Desktop/raspberry-pi-rgb-L2/button")
    press = Button(root, text = 'click here', image = photo, compound = LEFT, command=hello).pack(side = TOP)

    mainloop()
    
