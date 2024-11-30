# 4. Write a program to accept the age of n employees and count the number of persons in the following age group:
# (i) 26 - 35      (ii) 36 - 45       (iii) 46 - 55

n=int(input("Enter the no of employees : "))   
gr1, gr2, gr3 = 0, 0, 0 
for i in range(1,n+1):   
    age=int(input("Enter employee age : "))
    if (26<=age<=35):
        gr1+=1
    if (36<=age<=45):
        gr2+=1
    if (46<=age<=55):
        gr3+=1
        
print("Employees in age group 26 - 35 : ", gr1)        
print("Employees in age group 36 - 45 : ", gr2)        
print("Employees in age group 46 - 55 : ", gr3)        
        