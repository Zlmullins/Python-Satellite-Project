import matplotlib.pyplot as plt
import numpy as np

x1 = input("Enter the x position of the first satellite")
y1 = input("Enter the y position of the first satellite")
z1 = input("Enter the z position of the first satellite")
vx1 = input("Enter the x velocity of the first satellite")
vy1 = input("Enter the y velocity of the first satellite")
vz1 = input("Enter the z velocity of the first satellite")

x2 = input("Enter the x position of the second satellite")
y2 = input("Enter the y position of the second satellite")
z2 = input("Enter the z position of the second satellite")
vx2 = input("Enter the x velocity of the second satellite")
vy2 = input("Enter the y velocity of the second satellite")
vz2 = input("Enter the z velocity of the second satellite")

x3 = input("Enter the x position of the third satellite")
y3 = input("Enter the y position of the third satellite")
z3 = input("Enter the z position of the third satellite")
vx3 = input("Enter the x velocity of the third satellite")
vy3 = input("Enter the y velocity of the third satellite")
vz3 = input("Enter the z velocity of the third satellite")

plt.xlabel('X Displacement (km)')
plt.ylabel('Y Displacement (km)')
plt.title('Demonstration of a Three Body Orbit')
plt.grid(True)
plt.savefig('EP393Final.png')
plt.show()
