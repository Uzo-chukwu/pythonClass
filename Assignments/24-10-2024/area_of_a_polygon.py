import math


number_of_sides = int(input("Enter the number of sides: "))
lenght_of_a_side = int(input("Enter the lenght of a side: "))

n = number_of_sides
s = lenght_of_a_side
pi = 22/7

area = (n*s**2)/(4*(math.tan(pi/n)))

print("The area of the polygon = ",area)
