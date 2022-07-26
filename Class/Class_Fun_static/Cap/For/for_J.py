#J
class capital_alphabets:
    def __init__(self):
        pass
    def for_J(self,J,j):
        for row in range(J):#6
            for col in range(j):#7
                if (col==3 or row==0 )or(row==4 and col==1)or (row==5 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
