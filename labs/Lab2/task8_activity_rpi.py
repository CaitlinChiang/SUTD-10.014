from libdw import pyrebase
from sense_hat import SenseHat
from time import sleep

"""
TODO 8.0 Fill in the same authentication details as your partner
"""

projectid = "fill in"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "fill in"
email = "fill in"
password = "fill in"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)
db = firebase.database()
user = auth.refresh(user['refreshToken'])

s = SenseHat()

"""
TODO 8.4 Specify the RGB values of the colours
that you want to use
"""
r = (255, 0, 0)

"""
TODO 8.5 Use the RGB values specified to design your image
You may reuse your code from task 7
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
TODO 8.6 With your partner decide the key of your node.
See TODO 8.1. 
""" 
key = pass

try:
    while True:
        """
        TODO 8.7 Write code to retrieve the value from the node
        using the key. 
        """
        
        """
        TODO 8.8 Check the datatype of the value and 
        display the value on the screen
        """ 

        """
        TODO 8.9 Using the value obtained, 
        display the image acccordingly or clear the screen
        """ 

        """
        TODO 8.10 Pause execution for a short period e.g. 1 sec
        """ 
    pass 



except KeyboardInterrupt:
    print("ending the script and clearing the LED")
    s.clear()


    
