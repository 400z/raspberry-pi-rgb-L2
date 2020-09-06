from gpiozero import RGBLED
import psutil, time
led = RGBLED(15,14,18)

while True:
    try:
        cpu = psutil.cpu_percent()
        r = cpu / 100.0
        g = (100 - cpu)/100.0
        b = 0
        led.color = (r, g, b)
        time.sleep(0.1)

        
        temp = dict(psutil.sensors_temperatures())
        temp =list(temp['cpu_thermal'][0])
        temp = round(temp[1],1)
        print(temp)
    except KeyboardInterrupt:
        break

led.off()

    