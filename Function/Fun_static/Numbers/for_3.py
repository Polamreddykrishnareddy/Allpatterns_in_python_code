    #3
def for_3(a,b):
    for row in range(a):#8
        for col in range(b):#6
            if (row==0) or (row==1 and col==4) or (row==2 and col==3)or (row==3 and col==2)or (row==4 and col==3)or (row==5 and col==4) or row==6:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()


