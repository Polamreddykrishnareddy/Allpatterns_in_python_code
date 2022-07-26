#1.Square
print("Square")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==0) or (col==0)or(row==a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

#2. Rectangle
print("Rectangle")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a+3:
        if (row==0) or (col==0)or(row==a-1)or(col==a+2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

# 3.Triangle
print("Triangle")
a=int(input("Enter the number :"))
b=a+a
row=0
while row<a:
    col=0
    while col<b:
        if (row==a-1 and col<b-1)or(col+row==a-1)or(col-row==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

#4. Right Triangle
print("Right Triangle")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==a-1 )or(col+row==a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

# 5.Left Triangle
print("Left Triangle")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==a-1 )or(row-col==0)or(col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
# 6. Subtraction
print("Subtraction")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a+2:
        if (row==a//2) or (row==a-1)or(col==0 and row>a//2)or(col==a+1 and row>a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
# 7.Addison
print("Addison")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==a//2)or(col==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#8.Multiplication
print("multiplication")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row+col==a-1)or(row-col==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

#9. Division
print("Division")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row+col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
# 10.Floor division
print("Floor division")
a=int(input("Enter the number :"))
row=0
while row<a+1:
    col=0
    while col<a+2:
        if (row+col==a-1)or(row+col==a+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

#11. Right symbol
print("Right symbol")
a=int(input("Enter the only odd numbers  :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#12. Less symbol
print("Less symbol")
a=int(input("Enter the only odd numbers :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row-col==a//2)or(col+row==a//2)or(row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

#13. Greater than
print("Greater than")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if  (col-row==a//2)or(col+row==a//2+a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#14. Less-than
print("Less-than")
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row-col==a//2)or(col+row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
# 15.Diamond symbols
print("Diamond symbols")
a=int(input("Enter the only odd numbers :"))
row=0
while row<a:
    col=0
    while col<a:
        if  (col-row==a//2)or(col+row==a//2+a-1)or(row-col==a//2)or(col+row==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

