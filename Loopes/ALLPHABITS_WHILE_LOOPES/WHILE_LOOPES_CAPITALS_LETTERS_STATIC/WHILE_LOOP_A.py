#A
"""
row=0
while row<11:
    col =0
    while col<15:
        if (row==7 and col!=12 and col!=13 and col!=14 and col!=0 and col!=1 and col!=2 ) or (row==8 and col==2)or (row==9 and col==1)or (row==10 and col==0) or (row==8 and col==12 ) or (row==9 and col==13)or (row==10 and col==14)or (row==6 and col==4) or (row==5 and col==5 ) or (row==4 and col==6) or (row==6 and col==10) or (row==5 and col==9) or (row==4 and col==8)or (row==3 and col==7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col +=1
    row +=1
    print()
    """
a=5
b=10
row=0
while row<a:
    col=0
    while col<b:
        if (row+col==a-1)or (col==row+a-1)or (row==a//2 and col>a//2-1 and col<a+a//2): 
            print("*",end=" ")
        else:
            print(" ",end=" ")
        col+=1
    row+=1
    print()