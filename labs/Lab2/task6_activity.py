from sense_hat import SenseHat
from time import sleep

s = SenseHat()
try:
    
    while True:
        print("waiting for you to write code") 
        """
        TODO 6.1 Get the temperature reading and round it
        """

        """
        TODO 6.2 Decide the string to be displayed 
        """

        """
        TODO 6.3 Specify the RGB values for the colours you want to use 
        """

        """
        TODO 6.4 Write code to display the message on the LED matrix
        according to the requirements in the lab manual
        """        
        sleep(1)

#If Ctrl + C is pressed, this is executed        
except KeyboardInterrupt:
    print("ending the script and clearing the LED")
    s.clear()
