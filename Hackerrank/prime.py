num = int(input("Enter number to be checked"))
m = int(num/2)
flag = 0 

if num == 0 or num == 1:
    print("prime number")
    
else:
    for d in range (2,(m+1)):
        if(num % d == 0):
            flag = 1
    if flag == 0:
        print("Prime number")
    else:
        print("Not a prime number")
    
    