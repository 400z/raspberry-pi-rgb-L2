from gpiozero import RGBLED
import time
led = RGBLED(15,14,18)
while True:
    try:
        led.blue = 1
        for n in range(100):
            led.red = 0 + n/100
            time.sleep(0.02)
            if led.red == 0.4:
                break

        for n in range(35):
            led.red = 0.4 - n/100
            time.sleep(0.03)
            if led.red == 0.1:
                break

        for n in range(100):
            led.red = 0.1 + n/80
            time.sleep(0.01)
            if led.red == 1:
                break
        g = 1
        for n in range(100):
            led.blue = 1 - n/100
            time.sleep(0.01)
            if led.blue <= 0.15:
                led.green = 0 + (g/100)
                time.sleep(0.02)
                g = g +1
                continue


        time.sleep(0.5)
        led.off()
    
    except (KeyboardInterrupt, SystemExit):
        print("caught the interrupt")
        break
led.off()