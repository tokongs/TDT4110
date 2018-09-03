from math import *
height = 3
a = (3*height)/sqrt(6)

area = sqrt(3)*a**2
volume = (sqrt(2)*a**3)/12

print ("Et tetraeder med høyde", height, "har areal", area)
print ("Et tetraeder med høyde", height, "har volum", volume)

height = float(input("Skriv inn en høyde: "))

a = (3*height)/sqrt(6)

area = sqrt(3)*a**2
volume = (sqrt(2)*a**3)/12

print ("Et tetraeder med høyde", height, "har areal", area)
print ("Et tetraeder med høyde", height, "har volum", volume)