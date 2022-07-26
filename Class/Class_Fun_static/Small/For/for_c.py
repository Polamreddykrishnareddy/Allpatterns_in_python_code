    #c
class small_alphabits:
    def __init__(self):
        pass
    def for_c(self,c):
        for row in range(c):#7
            for col in range(c):#7
                if  (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

