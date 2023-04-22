 import machine
 import time
 
 LED = machine.Pin(13,machine.Pin.OUT)
 
 for i in range(100):
     LED.on()
     time.sleep()
     LED.off()
     time.sleep()
#Trial two
