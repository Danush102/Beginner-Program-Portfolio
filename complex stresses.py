#importing required library
import math

#getting user input
sigma_x=float(input("Enter the value of normal stress along x axis {sigma x} in Mega Pascals MPa\n "))
sigma_y=float(input("Enter the value of normal stress along y axis {sigma y} in Mega Pascals MPa\n "))
tow_xy=float(input("enter the value of shear stress along the xy plane\n"))
theta=float(input("What is the inclination of the normal of the inclined plane with x axis\n"))
angle_in_radians=math.radians(theta)

#calculating normal and shear stress
sigma_n= ((sigma_x+sigma_y)/2)+(((sigma_x-sigma_y)/2)*math.cos(2*angle_in_radians))+tow_xy*math.sin(2*angle_in_radians)
tow_nt= ((sigma_y-sigma_x)/2)*math.sin(2*angle_in_radians)+tow_xy*math.cos(2*angle_in_radians)

#calculating principal stresses
sigma_1=((sigma_x + sigma_y)/2)+ math.sqrt((((sigma_x-sigma_y)/2)*((sigma_x-sigma_y)/2))+(tow_xy*tow_xy))
sigma_2=((sigma_x + sigma_y)/2)- math.sqrt((((sigma_x-sigma_y)/2)*((sigma_x-sigma_y)/2))+(tow_xy*tow_xy))

#calculating maximum and minimum shear stresses
tow_1= math.sqrt((((sigma_x-sigma_y)/2)*((sigma_x-sigma_y)/2))+(tow_xy*tow_xy))
tow_2=- math.sqrt((((sigma_x-sigma_y)/2)*((sigma_x-sigma_y)/2))+(tow_xy*tow_xy))

#calculating orientation
theta_n=(1/2)*math.degrees(math.atan((2*tow_xy)/(sigma_x-sigma_y)))
theta_n1=theta_n
theta_n2= 90+theta_n

theta_t=(1/2)*math.degrees(math.atan((sigma_y-sigma_x)/(2*tow_xy)))
theta_t1=theta_t
theta_t2=90+theta_t

#printing output
print("the value of sigma n is:",end="")
print("%.4f" %sigma_n)
print("the value of tow nt is:",end="")
print("%.4f" %tow_nt)

print("the value of sigma 1 is:",end="")
print("%.4f" %sigma_1)
print("the value of sigma 2 is:",end="")
print("%.4f" %sigma_2)

print("the value of theta n1 is:",end="")
print("%.4f" %theta_n1)
print("the value of theta n2 is:",end="")
print("%.4f" %theta_n2)

print("the value of tow 1 is:",end="")
print("%.4f" %tow_1)
print("the value of tow 2 is:",end="")
print("%.4f" %tow_2)

print("the value of theta t1 is:",end="")
print("%.4f" %theta_t1)
print("the value of theta t2 is:",end="")
print("%.4f" %theta_t2)


