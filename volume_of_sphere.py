import math

def calculate_volume_of_sphere(radius):
    volume = ((4/3) * math.pi * (radius**3))
    return volume

radius1 = 30
print(f"The volume of a sphere with radius {radius1} is: {calculate_volume_of_sphere(radius1)}")

radius2 = 40
print(f"The volume of a sphere {radius2} is: {calculate_volume_of_sphere(radius2)}")