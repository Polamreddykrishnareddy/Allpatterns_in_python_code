    #8
class numbers:
    def __init__(self):
        pass
    def for_8(self,a,b):
        for row in range(a):#11
            for col in range(b):#6
                if (row==0 and col!=0 and col!=5) or (col==0 and row!=10 and row!=0 and col!=5 and row!=5)or (row==5 and col==1)or (row==5 and col==2)or (row==5 and col==3)or (row==5 and col==4) or(col==5  and row!=10 and row!=5 and row!=0)or (row==10 and col==1)or (row==10 and col==2)or (row==10 and col==3)or (row==10 and col==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


