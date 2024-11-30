# 1.write a program to search an element in a given list of numbers.
list=eval(input("Enter list elements : "))
ele=int(input("Enter the element : "))
n=len(list)   
for i in range(n):
    if(ele==list[i]):
        print("position : ", i+1)
if(ele not in list):
    print("not found")


# ---------------------- another method-------------------
list=[]
n=int(input("Enter the no of elements : "))
print("Enter the elements : ")
for i in range(n):
    elements=int(input())
    list.append(elements)
ele=int(input("Enter the element to search :"))  
flag=0 
for i in range(n):
    if(ele==list[i]):
        print("Element position is : ", i+1)
        flag+=1 
if(flag==0):
    print("Element not found")               