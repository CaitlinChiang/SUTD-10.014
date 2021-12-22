from sense_hat import SenseHat
from time import sleep

s = SenseHat()

red = (255, 0, 0)
try:
    
    while True:
        #what data type is the variable acceleration?
        acceleration = s.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']
        z = acceleration['z']

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            s.show_letter("!", red)
        else:
            s.clear()

#If Ctrl + C is pressed, this is executed        
except KeyboardInterrupt:
    print("ending the script and clearing the LED")
    s.clear()
