import math

def compound_interest(amount, rate, periods, time):
  f = amount * ((1 + (rate / periods))**(periods * time))
  return round(f, 3)

print(compound_interest(1, 0.03, 1, 1))
print(compound_interest(1, 0.12 ,12, 1))
print(compound_interest(1, 1 ,1000, 1))

def area_vol_cylinder(radius, length):
  area = math.pi * (radius**2)
  volume = area * length
  return round(area, 2), round(volume,2 )

print(area_vol_cylinder(1.0, 2.0))
print(area_vol_cylinder(2.0, 2.3))
print(area_vol_cylinder(1.5, 4))
print(area_vol_cylinder(2.2, 5.0))

def seconds_to_hours(seconds):
  hour = int(seconds / (60 * 60))
  minute = int((seconds - (hour * 3600)) / 60)
  seconds = int((seconds - (hour * 3600)) - (minute * 60))
  return hour, minute, seconds

print(seconds_to_hours(29500))
print(seconds_to_hours(7210))

def fahrenheit_to_celsius(f):
  c = (f - 32) * (5/9)

  if (c <= (-273.15)):
    return None
  
  return round(c, 2)

print(fahrenheit_to_celsius(-500))
print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(99)) 
print(fahrenheit_to_celsius(212))