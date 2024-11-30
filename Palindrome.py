while(1):
    n=int(input("Enter a number to check or 'q' to quit : "))
    if n=='q':
        break  
    else:       
        sum= 0
        temp=n
        while(n>0):    
            rem=n%10
            sum=sum*10+rem
            n=n//10
        if (sum==temp):
            print("It's a Palindrome number")   
        else:
            print("Not a Palindrome number")   
        
        