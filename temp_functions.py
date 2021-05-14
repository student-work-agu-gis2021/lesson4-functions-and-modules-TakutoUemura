"""I set up a function that converts from Fahrenheit to Celsius."""
def fahr_to_celsius(temp_fahrenheit):
  """Substituting a Fahrenheit value for temp_fahrenheit converts it to Celsius and returns that value."""
  converted_temp = (temp_fahrenheit - 32) / 1.8
  return converted_temp

"""Substituting Celsius for temp_celsius divides the temperature into one of four classes and returns the value in that class."""
def temp_classifier(temp_celsius):
  if temp_celsius < -2:
     return 0
  elif (temp_celsius >= -2) and (temp_celsius < 2):
     return 1
  elif (temp_celsius >= 2) and (temp_celsius < 15):
     return 2
  elif temp_celsius >= 15:
     return 3