from sense_hat import SenseHat
from time import sleep

s = SenseHat()

"""
TODO 7.1 Specify the RGB values of the colours that you want to use
"""
r = (255, 0, 0)
## and so on

"""
TODO 7.2 Use the RGB values specified to design your image
"""
pixel_image_A = [ r, r, r, r, r, r, r, r,
                  r, r, r, r, r, r, r, r,
                  r, r, r, r, r, r, r, r,
                  r, r, r, r, r, r, r, r,
                  r, r, r, r, r, r, r, r,
                  r, r, r, r, r, r, r, r,
                  r, r, r, r, r, r, r, r,
                  r, r, r, r, r, r, r, r]

pixel_image_B = []

"""
TODO 7.3 Increase this value to larger than one but below two.
See that you need to shake the SenseHat harder to change the image.
"""
threshold = 1.0

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

        """
        TODO 7.4 Write code to display the image of your choice
        on the LED matrix in the if/else statement
        """
        if x > threshold or y > threshold or z > threshold:
            pass
        else:
            pass

        """
        TODO 7.5 Display the acceleration values on the screen
        for troubleshooting purposes
        """
        
#If Ctrl + C is pressed, this is executed        
except KeyboardInterrupt:
    print("ending the script and clearing the LED")
    s.clear()
