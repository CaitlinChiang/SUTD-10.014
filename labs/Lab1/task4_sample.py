from libdw import pyrebase

projectid = "mycdtdproject-d2fb4"
dburl = "https://mycdtdproject-d2fb4-default-rtdb.asia-southeast1.firebasedatabase.app"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyDUSQ-19M3KEVBwmTxJVfJH_KLe2MsjExE"
email = "chiangcaitlin2003@gmail.com"
password = "CaitlinSUTDPython" 

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

key = "data"

print("Would you like to display image A or B?")
value = input("Would you like to display image A or B?: ")
if value == 'A':
  value = 1
else: 
  value = 2

db.child(key).set(int(value), user['idToken'])
