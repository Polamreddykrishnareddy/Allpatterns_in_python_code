
#a
b=int(input("Enter the number :"))
a=3
row=0
while row<a+b:
    col=0
    while col<b:
        if(row==0 and col<b-2 and col>0)or(col==b-2 and row>0)or(row==1 and col==0)or(row==(a+b)-2 and col<b-1 and col>0)or(row==(a+b)//2-1 and col<b-1 and col>0)or(col==0 and row>b//2 and row<(a+b)-2) or(row==a+b-1 and col>b-2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#b
a=int(input("Enter the number :"))
b=a+3
row=0
while row<b:
    col=0
    while col<a:
        if (col==0 and row<b-1)or(row==b//2 and col<a-1)or(row==b-1 and col>0 and col<a-1) or (col==a-1 and row>b//2 and row<b-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#c
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==0 and col>0) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#d
a=int(input("Enter the number :"))
b=a+a
row=0
while row<b:
    col=0
    while col<a:
        if (row==b//2 and col>0) or(col==0 and row>a and row<b-1) or(row==b-1 and col>0)or col==a-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#e
a=int(input("Enter the6 or 6Up number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==0 and col>0 and col<a-1)or(row==a//2-1 and col<a-1) or(col==0 and row>0 and row<a-1) or(row==a-1 and col>0)or (col==a-1 and row>0 and row<a//2-1):#(col-row==a//2 and row<a//2-1)  :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
#f
a=int(input("Enter the number :"))
b=a+3
row=0
while row<b:
    col=0
    while col<a:
        if (col==a//2-1 and row>0)or (row==b//2) or row==0 and col>a//2-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#g
a=int(input("Enter the number :"))
b=a+3
row=0
while row<b:
    col=0
    while col<a:
        if (col==a-1 ) or (row==0 and col>1) or(col==1 and row>0 and row<a//2)or(row==a//2 and col>1) or (row-col==3 and col>a//2-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#h
a=int(input("Enter the number :"))
b=a+a
row=0
while row<b:
    col=0
    while col<a:
        if (col==0) or (row==b//2)or(col==a-1 and row>b//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#i
a=int(input("Enter the number :"))
b=a+3
row=0
while row<b:
    col=0
    while col<a+1:
        if (col==a//2 and row>1)or (row==b-1) or(col==a//2+1 and row>1) or(row==0 and col>a//2-1 and col<a-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#j
a=int(input("Enter the number :"))
b=a+3
row=0
while row<b:
    col=0
    while col<a:
        if  (col==a//2) or (row==0)or (row-col==a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#k
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if  (col==0) or (row-col==a//2-1) or (row+col==a//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#l
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if( col==a//2) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#m
a=int(input("Enter the number :"))
b=a+a
row=0
while row<a:
    col=0
    while col<b:
        if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<b//2 and col>1)or (col==b//2 and row>0)or (row==0 and col>b//2 and col<b-1)or(col==b-1 and row>0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#n
a=int(input("Enter the number :"))  
row=0
while row<a:
    col=0
    while col<a:
        if (col==1 and row>0)or(row-col==0 and row<1) or (col==a-1 and row>0) or(row==0 and col<a-1 and col>1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#o
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1 and row>0 and row<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#p
a=int(input("Enter the number :"))
row=0
while row<a+a:
    col=0
    while col<a:
        if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0)or(col==a-1 and row>0 and row<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#q
a=int(input("Enter the number :"))
row=0
while row<a+3:
    col=0
    while col<a:
        if (row==0 and col>0 and col<a-1)or(row==a-1 and col>0 and col<a-1)or (col==0 and row>0 and row<a-1)or(col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#r
a=int(input("Enter the number :"))
b=a+1
row=0
while row<b:
    col=0
    while col<a:
        if (row==col) or (row+col==a-1)or(row==a and col>0 and col<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()

#s
a=int(input("Enter the number :"))
b=a+a
row=0
while row<b:
    col=0
    while col<a:
        if  (row==0 and col>0) or (col==0 and row>0 and row<b//2-1) or(row==b//2-1 and col>0 and col<a-1) or(col==a-1 and row>a-1 and row<b-2)or(row==b-2 and col<a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#t
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (col==a//2)or(row==a//2-1)or(row==a-1 and col>a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#u
a=int(input("Enter the number :"))
row=0
while row<a+1:
    col=0
    while col<a+1:
        if (col==0 and row<a-1) or (col==a-1 and row<a ) or (row==a-1 and col>0 and col<a-1) or(row==a and col==a):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#v
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row+col==a-1 and row<a//2+1)or(row-col==0 and row<a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#w
a=int(input("Enter the number :"))
b=a+2
row=0
while row<b:
    col=0
    while col<b:
        if (col==0) or (row-col==0 and row>a//2) or(col==b-1) or(row+col==b-1 and row>a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#x   
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==col) or (row+col==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#y
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row-col==0 and col<a//2)or (row+col==a-1 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    
#z
a=int(input("Enter the number :"))
row=0
while row<a:
    col=0
    while col<a:
        if (row==0 )or (row+col==a-1 ) or(row==a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()
    