
#a
b=int(input("Enter the number :"))#a
a=3
for row in range(a+b):
    for col in range(b):
        if(row==0 and col<b-2 and col>0)or(col==b-2 and row>0)or(row==1 and col==0)or(row==(a+b)-2 and col<b-1 and col>0)or(row==(a+b)//2-1 and col<b-1 and col>0)or(col==0 and row>b//2 and row<(a+b)-2) or(row==a+b-1 and col>b-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#b
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a):
        if (col==0 and row<b-1)or(row==b//2 and col<a-1)or(row==b-1 and col>0 and col<a-1) or (col==a-1 and row>b//2 and row<b-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#c
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==0 and col>0) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#d
a=int(input("Enter the number :"))
b=a+a
for row in range(b):
    for col in range(a):
        if (row==b//2 and col>0) or(col==0 and row>a and row<b-1) or(row==b-1 and col>0)or col==a-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#e 
a=int(input("Enter the 6 or 6Up number :"))
for row in range(a):
    for col in range(a):
        if (row==0 and col>0 and col<a-1)or(row==a//2-1 and col<a-1) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0)or (col==a-1 and row>0 and row<a//2-1):#(col-row==a//2 and row<a//2-1)  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#f
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a):
        if (col==a//2-1 and row>0)or (row==b//2) or row==0 and col>a//2-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#g
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a):
        if (col==a-1 ) or (row==0 and col>1) or(col==1 and row>0 and row<a//2)or(row==a//2 and col>1) or (row-col==3 and col>a//2-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
   
#h
a=int(input("Enter the number :"))
b=a+a
for row in range(b):
    for col in range(a):
        if (col==0) or (row==b//2 and col<a-1)or(col==a-1 and row>b//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#i
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a+1):
        if (col==a//2 and row>1)or (row==b-1) or(col==a//2+1 and row>1) or(row==0 and col>a//2-1 and col<a-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#j
a=int(input("Enter the number :"))
b=a+3
for row in range(b):
    for col in range(a):
        if  (col==a//2) or (row==0)or (row-col==a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#k
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        #if  (col==0) or (row-col==a//2) or (row+col==a//2):
        if  (col==0) or (row-col==a//2-1) or (row+col==a//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#l
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if( col==a//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

#m
a=int(input("Enter the number :"))
b=a+a
for row in range(a):
    for col in range(b):
        if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<b//2 and col>1)or (col==b//2 and row>0)or (row==0 and col>b//2 and col<b-1)or(col==b-1 and row>0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

#n
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (col==1 and row>0)or(row-col==0 and row<1) or (col==a-1 and row>0) or(row==0 and col<a-1 and col>1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#o
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1 and row>0 and row<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
#p
a=int(input("Enter the number :"))
for row in range(a+a):
    for col in range(a):
        if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0)or(col==a-1 and row>0 and row<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#q
a=int(input("Enter the number :"))
for row in range(a+3):
    for col in range(a):
        if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#r
a=int(input("Enter the number :"))
b=a+1
for row in range(b):
    for col in range(a):
        if (row==col) or (row+col==a-1)or(row==a and col>0 and col<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#s
a=int(input("Enter the number :"))
b=a+a
for row in range(b):
    for col in range(a):
        if  (row==0 and col>0) or (col==0 and row>0 and row<b//2-1) or(row==b//2-1 and col>0 and col<a-1) or(col==a-1 and row>a-1 and row<b-2)or(row==b-2 and col<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
   
#t
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (col==a//2 and row<a-1)or(row==a//2-1)or(row==a-1 and col>a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
 
#u
a=int(input("Enter the number :"))
for row in range(a+1):
    for col in range(a+1):
        if (col==0 and row<a-1) or (col==a-1 and row<a ) or (row==a-1 and col>0 and col<a-1) or(row==a and col==a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# v padding
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row+col==a-1 and row<a//2+1)or(row-col==0 and row<a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#w
a=int(input("Enter the number :"))
b=a+2
for row in range(b):
    for col in range(b):
        if (col==0) or (row-col==0 and row>a//2) or(col==b-1) or(row+col==b-1 and row>a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
  
#x
    
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==col) or (row+col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    

#y
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row-col==0 and col<a//2)or (row+col==a-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#z
a=int(input("Enter the number :"))
for row in range(a):
    for col in range(a):
        if (row==0 )or (row+col==a-1 ) or(row==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
