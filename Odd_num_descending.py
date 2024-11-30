# 7. Write a short program to print first n odd numbers in descending order
list=[]
n=int(input("Enter no.  : "))
for i in range(1,n+1):
    if (i%2!=0):
        list.append(i)
# list.reverse()  
list=list[::-1]     #another method instead of line no.7        
print(list)        

