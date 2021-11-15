
# Create a simple python program to collect information from a users and print it
# Information must be : user name, car name, register number, car color ( using dictionary )
# Printing of information must be in a good alignment

print("\n------------ Collecting User's Data ------------\n")
n = int(input("Enter How many User's are there :"))
userName = {}
carName = {}
regNo = {}
carColor = {}
for i in range(n):
    userName[i] = input("\nEnter Your Username : ")
    carName[i] = input("Enter Your Car Name : ")
    regNo[i] = input("Enter Your Register Number : ")
    carColor[i] = input("Enter the Color of Your Car : ")
print("\n")
print("------------ User's Information ------------\n")
for i in range(n):
    print("Data Given By the User " + str(i+1))
    print("Username         : " + userName[i])
    print("Car Name         : " + carName[i])
    print("Register Number  : " + userName[i])
    print("Car Color        : " + carColor[i])
    print("\n")
