
# 2. Python program to print even length words in a string
from posixpath import split
def Evenlen(s):
    s=s.split()
    for i in s:
        if (len(i)%2==0):
            print(i)
s=input("Enter the string : ")  
Evenlen(s) 