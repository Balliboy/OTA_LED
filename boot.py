 import machine
 import time
 
 LED = machine.Pin(2,machine.Pin.OUT)
 
 for i in range(100)
     LED.value(1)
     time.sleep()
     LED.value(0)
     time.sleep(1)