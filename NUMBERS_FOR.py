#1
a=int(input("Enter the number :"))
for row in range(a+2):
    for col in range(a):
        if (col==a//2)or(row==a+1)or(row+col==a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#2
a=int(input("Enter the number :"))
b=a+2
for row in range(b):
    for col in range(a):
        if (row==0 and col>1 and col<a-1)or(row==a//2+1 and col>1 and col<a-1)or(col==1 and row>0 and row<a//2+1)or(col==a-1 and row>0 and row<a//2+1)or(row+col==a+1)or(row==a+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#3
a=int(input("Enter the number :"))
b=a+a
for row in range(b):
    for col in range(a):
        if (row==0 and col<a-1)or(row==b//2 and col<a-1)or(row==b-1 and col<a-1)or(col==a-1 and row!=a and row>0 and row<b-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#4
a=int(input("Enter the number :"))
for row in range(a+2):
    for col in range(a+1):
        if (col==a-1)or(row==a-1)or(row+col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#5
a=int(input("Enter the number :"))
b=a+a
for row in range(b):
    for col in range(a):
        if (row==0)or(col==0 and row<a-1)or(row==a-1 and col<a-1)or(col==a-1 and row>a-1 and row<b-1)or(row==b-1 and col<a-1):#5
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#6
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a):
        if (row==b-1 and col>0 and col<a-1)or(row==b//2  and col>0 and col<a-1)or(col==0 and row>1 and  row<b-1)or(col==a-1 and row>b//2 and row<b-1)or(row==0 and col==2)or(row==1 and col==1):#6
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#7
a=int(input("Ente the number : "))
for row in range(a):
    for col in range(a):
        if (row==0)or(row+col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#8
a=int(input("Ente the number : "))
b=a+4
for row in range(b):
    for col in range(a):
        if (row==0 and col>0 and col<a-1)or(row==b//2 and col>0 and col<a-1)or(row==b-1 and col>0 and col<a-1)or(col==0 and row!=b//2 and row>0 and row<b-1)or(col==a-1 and row!=b//2 and row<b-1 and row>0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#9
a=int(input("Ente the number : "))
b=a+4
for row in range(b):
    for col in range(a):
        if(row==0 and col>0 and col<a-1)or(row==b//2 and col>0 and col<a-1)or(col==a-1 and row>0)or(col==0 and row>0 and row<b//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#10
a=int(input("Enter the number :"))
b=a+3
for row in range(a+3):
    for col in range(b):
        if (col==a//2)or(row==(a+2) and col<a)or(row+col==a//2)or(row==1 and col>b//2 and col<b-1)or(col==b-1 and row>1 and row<a) or(row==a and col>b//2 and col<b-1 )or(col==b//2 and row>1 and row<a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()