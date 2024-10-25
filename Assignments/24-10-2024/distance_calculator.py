import math

latitude_one = float(input("Enter the latitude of coordinate 1: "))
longitude_one =  float(input("Enter the longitude of coordinate 1: "))
latitude_two =  float(input("Enter the latitude of coordinate 2: "))
longitude_two =  float(input("Enter the longitide of coordinate 2: "))
radius = 6371.01

distance = radius * math.acos(math.sin(latitude_one) * math.sin(latitude_two) + math.cos(latitude_one) * math.cos(latitude_two) * math.cos(longitude_one - longitude_two))

print(distance)