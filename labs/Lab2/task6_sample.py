from sense_hat import SenseHat
from time import sleep

s = SenseHat()
try:
    
    while True:
        print(s.get_temperature())
        sleep(1)

#If Ctrl + C is pressed, this is executed        
except KeyboardInterrupt:
    print("ending the script")
