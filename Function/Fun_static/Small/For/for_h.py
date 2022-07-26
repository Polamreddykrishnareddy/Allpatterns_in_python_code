#h
def for_h(h,H):
    for row in range(h):# 11   
        for col in range(H):#10
            if (col==0) or (row==5 and col==1)or(row==5 and col==2)or(row==5 and col==3)or(row==5 and col==4)or(row==6 and col==5)or(row==7 and col==5)or(row==8 and col==5)or(row==9 and col==5)or(row==10 and col==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

