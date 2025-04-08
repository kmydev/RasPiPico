import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

while (True):
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.25)
