    #D
class capital_alphabets:
    def __init__(self):
        pass
    def for_D(self,D):
        for row in range(D):#6
            for col in range(D):#6
                if (col==0 or col==1 and row!=1 and row!=2 and row!=3 and row!=4)or (col==2 and row!=1 and row!=2 and row!=3 and row!=4) or (col==3 and row!=0 and row!=2 and row!=3  and row!=5) or (col==4 and row!=0 and row!=1 and row!=4  and row!=5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
