#M
def for_M(M,m):
    for row in range(M):#7
        for col in range(m):#11
            if (col==0 )or (row==3 and col==7)or (row==2 and col==8)or (row==1 and col==9)or (col==10)or(row==4 and col==6)or(row==1 and col==1)or(row==2 and col==2)or(row==3 and col==3)or(row==4 and col==4)or (row==5 and col==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()




