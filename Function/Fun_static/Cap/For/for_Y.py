    #Y
def for_Y(Y):
    for row in range(Y):#11
        for col in range(Y):#11
            if (row==col and col<6)or(col==5 and row>5) or (row==0 and col==10)or (row==1 and col==9)or (row==2 and col==8)or (row==3 and col==7)or (row==4 and col==6):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


