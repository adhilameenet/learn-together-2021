
from math import pi,pow

def area_of_rectangle():
    l = int(input("Length of the Rectangle  :"))
    b = int(input("Breadth of the Rectangle :"))
    area = l * b
    print(f'Area of the Rectangle    :{area}')

def area_of_triangle():
    b = int(input("Base of the triangle     :"))
    h = int(input("Height of the triangle   :"))
    area = 0.5 * b * h
    print(f'Area of the Triangle     :{area}')

def area_of_square():
    a = int(input("Side of the Square       :"))
    area = pow(a,2)
    print(f'Area of the Square       :{area}')

def area_of_circle():
    r = int(input("Radius of the circle     :"))
    area = pi * r * r
    print(f'Area of the Circle       :{area}')
