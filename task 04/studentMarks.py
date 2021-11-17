
'''
    Create a simple python program to input Name, Marks in 3 subject of 5 Students (each subject out of 100) then print :
    - Name
    - Sum of 3 subjects
    - Status :  Pass/Fail ( student need at least 60 in 3 subject to Pass )
'''

print("----- Collecting Student Details -----")
name = {}
total_mark = {}
for i in range(5):  
    print("Student : ",i+1)
    name[i] = input("Enter Your Name : ")
    mark_1 = int(input("Enter First Subject Mark : "))
    mark_2 = int(input("Enter Second Subject Mark : "))
    mark_3 = int(input("Enter Third Subject Mark : "))
    total_mark[i] = mark_1 + mark_2 + mark_3
    print("\n")
print("\n----- Student Exam Results -----")
for i in range(5):
    print("Student           : ",i+1)
    print("Name              : ",name[i])
    print("Sum of 3 Subjects : ",total_mark[i])
    if total_mark[i] >= 60 :
        print("Status            :  Pass")
    else :
        print("Status            :  Fail")
    print("\n")

