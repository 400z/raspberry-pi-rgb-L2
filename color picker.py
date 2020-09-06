from gpiozero import RGBLED
import time
led = RGBLED(15,14,18)


led.color = (0,0,1)
time.sleep(2)
led.off()