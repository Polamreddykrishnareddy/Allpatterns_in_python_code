#d
class small_alphabits:
    def __init__(self):
        pass
    def for_d(self,d,D):
        for row in range(d):#10
            for col in range(D):#7
                if (col==6 and row!=9)or (row==9 and col!=6 and col!=0)or (row==5 and col!=0) or (row==6 and col==0)or (row==7 and col==0)or (row==8 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

