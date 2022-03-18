#Problem Statement 1:- Write a python program to accept marks of five subjects from student.
# Calculate percentage and display result like First Class,Second Class,Pass,Fail using decision making 
# statements.

print("::::::::::::::::::::::Enter your marks out off 80::::::::::::::::::::::")
a = int(input("Enter Maths Marks"))
b = int(input("Enter Java Marks"))
c = int(input("Enter SQL Marks"))
d = int(input("Enter OS Marks"))
e = int(input("Enter Prolog Marks"))
sum= a + b + c + d + e
Percentage = (sum/400)*100

print("You Percentage is",Percentage,"%")

if(Percentage >= 40):
    print(":::::::::::Your Pass:::::::::::")
elif(Percentage > 80):
    print(":::::::::::First Class:::::::::::")
elif(Percentage > 50 and Percentage < 80):
    print(":::::::::::Second Class:::::::::::")
else:
    print(":::::::::::Your Fail:::::::::::")
