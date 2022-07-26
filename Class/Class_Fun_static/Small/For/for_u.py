    #u
class small_alphabits:
    def __init__(self):
        pass
    def for_u(self,u):
        for row in range(u):#7
            for col in range(u):#7
                if (col==0 and row!=6) or (col==5  and row!=6 ) or (row==6 and col==1) or (row==6 and col==2) or (row==6 and col==3) or (row==6 and col==4)or(row==6 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

