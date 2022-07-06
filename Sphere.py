# Joseph Rodriguez 
# jrodr273@ucsc.edu
# programming assignment 1
# My program calculates the volume and surface area of a sphere based on the
# raidus you enter.


from math import pi as p
r=float(input('Enter the radius of the sphere: '))
volume=((4/3)*p*(r**3))
surface_area=4*p*(r**2)

print('The volume is:',volume)
print('The surface area is:',surface_area)
