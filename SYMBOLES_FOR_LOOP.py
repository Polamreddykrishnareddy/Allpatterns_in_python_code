#1.Square
print("Square")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==0) or (col==0)or(row==a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#2. Rectangle
print("Rectangle")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a+3):
        if (row==0) or (col==0)or(row==a-1)or(col==a+2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# 3.Triangle
print("Triangle")
a=int(input("Enter the number :"))
b=a+a
for row in range(a):
    for col in range(b):
        if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#4. Right Triangle
print("Right Triangle")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==a-1 )or(col+row==a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# 5.Left Triangle
print("Left Triangle")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==a-1 )or(row-col==0)or(col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
# 6. Subtraction
print("Subtraction")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a+2):
        if (row==a//2) or (row==a-1)or(col==0 and row>a//2)or(col==a+1 and row>a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# 7.Addison
print("Addison")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        #if (row==a//2 and col!=a//2+1) or (row==a-1 and col!=a//2+1 )or(col==0 and row>a//2 and row<a)or(col==a+1 and row>a//2 and row<a)or(col==a//2)or(col==b//2-1):
        if (row==a//2)or(col==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#8.Multiplication
print("multiplication")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row+col==a-1)or(row-col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#9. Division
print("Division")
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row+col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# 10.Floor division
print("Floor division")
a=int(input("Enter the number :"))
for row in range(a+1):
    for col in range(a+2):
        if (row+col==a-1)or(row+col==a+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

#11. Right symbol
print("Right symbol")
a=int(input("Enter the only odd numbers :"))
for row in range(a):
    for col in range(a):
        if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#12. Less symbol
print("Less symbol")
a=int(input("Enter the only odd numbers :"))
for row in range(a):
    for col in range(a):
        if (row-col==a//2)or(col+row==a//2)or(row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#13. Greater than
print("Greater than")
a=int(input("Enter the  numbers :"))
for row in range(a):
    for col in range(a):
        if  (col-row==a//2)or(col+row==a//2+a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#14. Less-than
print("Less-than")
a=int(input("Enter the  numbers :"))
for row in range(a):
    for col in range(a):
        if (row-col==a//2)or(col+row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
# 15.Diamond symbols
print("Diamond symbols")
a=int(input("Enter the only odd numbers :"))
for row in range(a):
    for col in range(a):
        if  (col-row==a//2)or(col+row==a//2+a-1)or(row-col==a//2)or(col+row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    