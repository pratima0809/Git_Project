
import math

# Function to calculate the volume of a cylinder
def cylinder_volume(radius, height):
    return math.pi * (radius ** 2) * height

# Input radius and height
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))

# Calculate volume
volume = cylinder_volume(radius, height)

print("Hello World")
print(f"The volume of the cylinder with radius {radius} and height {height} is {volume:.2f}")


