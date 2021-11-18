
'''
Create a simple menu driven python program to find area of rectangle, triangle, square, circle 
- Need seperate functions for each shape to calculate area and name the file as 'functions.py'
- Need a menu to select shape by user to find area
- create a file name 'main.py' in same folder to access user input and 
  import the module 'functions' (the 'functions.py'  file)
'''


import functions

print("\n----- MENU -----")
print("1 : Rectangle")
print("2 : Triangle")
print("3 : Square")
print("4 : Circle")

option = int(input("\nSelect an Option : ")) 

if option == 1 :
    functions.area_of_rectangle()
elif option == 2 :
    functions.area_of_triangle()
elif option == 3 :
    functions.area_of_square()
elif option == 4 :
    functions.area_of_circle()
else :
    print("Invalid Choice..!")

