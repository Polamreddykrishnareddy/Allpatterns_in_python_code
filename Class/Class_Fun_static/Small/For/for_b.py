#b
class small_alphabits:
    def __init__(self):
        pass
    def for_b(self,b,B):
        for row in range(b):#11
            for col in range(B):#5
                if (col==0)or (row==6 and col==1)or (row==6 and col==2)or (row==6 and col==3)or (row==7 and col==4)or (row==8 and col==4)or (row==9 and col==4)or(row==10 and col==3)or(row==10 and col==2)or(row==10 and col==1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

