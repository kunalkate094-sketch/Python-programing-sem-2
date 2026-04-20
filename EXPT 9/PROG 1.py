import math

# Take input from the user
num = float(input("Enter a number for squre root and power calculation:"))
power = float(input("Enter the exponent value:"))

angle_deg = float(input("Enter an angle in degrees in degrees for trigonometric function:"))

# Squre root
sqrt_value = math.sqrt(num)
print(f"Squre root of {num} is {sqrt_value}")

# Power
power_value = math.pow(num,power)
print(f"{num} raised to the power {power} is {power_value}")

# Convert angle to radians for trig function 
angle_red = math.radians(angle_deg)

# Trigonometric function
sin_value = math.sin(angle_red)
cos_value = math.cos(angle_red)
tan_value = math.tan(angle_red)

print(f"Sin({angle_deg}°) = {sin_value}")
print(f"Cos({angle_deg}°) = {cos_value}")
print(f"Tan({angle_deg}°) = {tan_value}")
