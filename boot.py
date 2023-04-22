 import machine
 import time
 
 LED = machine.Pin(13,machine.Pin.OUT)
 
 for i in range(100):
     LED.value(4)
     time.sleep()
     LED.value(4)
     time.sleep(1)
