#q
for row in range(13):
    for col in range(8):
        if (col==5 or row==0 and col!=0 and col!=6 and col!=7) or (row==1 and col==0)or (row==2 and col==0)or (row==3 and col==0)or (row==4 and col==0) or (row==5 and col!=0 and col!=6 and col!=7) or (row==11 and col==6) or (row==10 and col==7):#p
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
