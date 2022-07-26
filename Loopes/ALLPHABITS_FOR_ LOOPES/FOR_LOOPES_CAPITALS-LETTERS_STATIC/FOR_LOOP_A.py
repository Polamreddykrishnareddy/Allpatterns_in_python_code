#A
for row in range(11):
    for col in range(15):
        if (row==7 and col!=12 and col!=13 and col!=14 and col!=0 and col!=1 and col!=2 ) or (row==8 and col==2)or (row==9 and col==1)or (row==10 and col==0) or (row==8 and col==12 ) or (row==9 and col==13)or (row==10 and col==14)or (row==6 and col==4) or (row==5 and col==5 ) or (row==4 and col==6) or (row==6 and col==10) or (row==5 and col==9) or (row==4 and col==8)or (row==3 and col==7):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    # or
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3)and (col>0 and col<4)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
