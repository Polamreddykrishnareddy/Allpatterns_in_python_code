    #C
class capital_alphabets:
    def __init__(self):
        pass
    def for_C(self,C):
        for row in range(C):#7
            for col in range(C):#7
                if (row==0 and col==3)or (row==0 and col==4)or (row==0 and col==5) or(row==0 and col==2) or (row==1 and col==1) or (row==2 and col==1) or (row==3 and col==1)or(row==4 and col==3) or(row==4 and col==4)or(row==4 and col==5)or(row==4 and col==2):
                     print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

