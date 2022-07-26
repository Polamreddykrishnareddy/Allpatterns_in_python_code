    #1
class numbers:
    def __init__(self):
        pass
    def for_1(self,_1):
        for row in range(_1):#10
            for col in range(_1):#10
                if (col==5) or(row==1 and col==4)or(row==2 and col==3) or (row==3 and col==2)or (row==9):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


