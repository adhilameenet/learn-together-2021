
# Create a simple python program to input a number by user then check the following :
# - The Number is even or odd
# - Negative or Positive
# - Less than or Greater than 10

num = int(input("Enter a Number :"))
print("The Number is :")
# Checking positive or negative
if num > 0:
   print("- Positive")
elif num == 0:
   print("- Zero")
else:
   print("- Negative")
# Checking Even or Odd  
if (num % 2) == 0:
   print("- Even")
else:
   print("- Odd")
# Checking greater or less than 10
if (num > 10) :
    print("- Greater than 10")
elif num == 10 :
    print("- Number is 10")
else :
    print("- Less than 10")
