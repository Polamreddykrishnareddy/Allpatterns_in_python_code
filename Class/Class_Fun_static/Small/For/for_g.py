    #g
class small_alphabits:
    def __init__(self):
        pass
    def for_g(self,g):
        for row in range(g):#10
            for col in range(g):#10
                if (col==9 and row!=0)or (row==9 and col==8)or (row==8 and col==7) or (row==0 and col==8)or (row==0 and col==7)or (row==0 and col==6)or (row==0 and col==5) or (row==1 and col==4)or (row==2 and col==4)or (row==3 and col==4)or (row==4 and col==5) or (row==4 and col==6) or (row==4 and col==7) or (row==4 and col==8):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

