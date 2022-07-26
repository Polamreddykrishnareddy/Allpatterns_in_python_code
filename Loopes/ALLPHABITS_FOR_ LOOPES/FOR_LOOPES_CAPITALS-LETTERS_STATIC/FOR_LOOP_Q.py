#Q
for row in range(8):
    for col in range(8):
        if (col==1 and row==0)or (col==2 and row==0)or (col==3 and row==0)or (col==4 and row==1)or (col==4 and row==2)or (col==4 and row==3)or (col==5 and row==5)or (col==6 and row==6)or (col==1 and row==4)or (col==2 and row==4)or (col==3 and row==4)or (col==4 and row==4)or (col==0 and row==1)or (col==0 and row==2)or (col==0 and row==3)or (col==3 and row==3)or (col==2 and row==2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""    
a=int(input("enter the number :"))
b=a+a-1
for row in range(a):
    for col in range(b):
        if (row==a-1)or (row+col==a-1)or (col==row+a-1) :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    """