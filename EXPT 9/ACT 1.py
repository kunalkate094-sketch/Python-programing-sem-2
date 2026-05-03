import math
try:
    print("Enter coordinates of first point:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    print("Enter coordinates of second point:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    # Distance formula
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print("Distance between the two points is:", distance)
except ValueError:
    print("Error: Please enter valid numeric values.")
finally:
    print("Program executed successfully.")
