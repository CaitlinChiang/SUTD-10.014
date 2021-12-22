import math

class PolarComplex:
  def __init__(self, r, theta):
    self.r = r
    self.theta = theta

  def get_modulus(self):
    return self.r

  def get_argument(self):
    return self.theta

  def get_real(self):
    return self.r * math.cos(self.theta)

  def get_imaginary(self):
    return self.r * math.sin(self.theta)

  def get_cartesian_form(self):
    return complex(self.get_real(), self.get_imaginary())

  def get_polar_form_string(self):
    return "{modulus} exp( j*{argument} )".format(modulus = format(self.r, ".3f"), argument = format(self.theta, ".3f"))

a = PolarComplex(5, math.pi/3)
b = PolarComplex(10/3, math.pi/6)
print(a.get_polar_form_string())
print(b.get_polar_form_string())
