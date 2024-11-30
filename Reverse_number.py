# Write a program to input a 2 digits number and prints reverse of that number

n = int(input("Enter the number: "))
sum=0
while (n>0):
    rem = n%10
    sum=sum*10+rem
    n=n//10
rev_num=sum    
print("Reverse number is = ", rev_num)    


