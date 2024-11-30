# 2. Write a program that asks the user for two numbers and prints Close if the numbers are within .001
# of each other and Not close otherwise.

a=float(input("Enter the 1st number : "))
b=float(input("Enter the 2nd number : "))
diff=0
if (a>b):
    diff=a-b
else:
    diff=b-a    
if (diff<=0.001):
    print("They are close number")
else:
    print("They are not close number")
        