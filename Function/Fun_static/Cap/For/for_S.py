#S
def for_S(S,s):
    for row in range(S):#9
        for col in range(s):#7
            if (row==0 and col==3)or(row==0 and col==4)or (row==0 and col==5) or(row==0 and col==2) or (row==1 and col==1) or (row==2 and col==1) or (row==3 and col==1)or(row==4 and col==3) or(row==4 and col==4)or(row==4 and col==5)or(row==4 and col==2) or (row==5 and col==6) or (row==6 and col==6) or (row==7 and col==6) or (row==8 and col==5)or (row==8 and col==4)or (row==8 and col==3)or (row==8 and col==2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


