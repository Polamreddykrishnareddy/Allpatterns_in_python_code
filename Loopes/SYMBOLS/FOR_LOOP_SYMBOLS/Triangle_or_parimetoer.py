
#Triangle or parimetoer 
print("Triangle or parimetoer ")
a=int(input("Enter the number :"))
b=a+a
for row in range(a):
    for col in range(b):
        if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
   
n = int(input("Enter number of rows:")) 
for i in range(1,n+1): 
    print(" " * (n-i),end="") 
    print("* "*i)