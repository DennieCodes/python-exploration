import math

class OneDivisionError(RuntimeError):
   pass

def fifty_by(number):
    if number == 1:
       raise OneDivisionError
    try:
      return 50 / number
    except ZeroDivisionError:
      print("Error: Invalid argument")
      return math.inf
    except TypeError:
       print("Error: Why did you give me that?")
       return math.nan

print(fifty_by(5))
print(fifty_by(15))
print(fifty_by(0))
print(fifty_by(1))
print(fifty_by("A"))
