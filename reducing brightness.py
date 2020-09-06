#reducing brightness
from gpiozero import RGBLED
from time import sleep
led = RGBLED(15,14,18)

for n in range(100):
    led.blue = 1 - n/20
    sleep(0.05)
    if led.blue == 0:
        break
    
print("finished")