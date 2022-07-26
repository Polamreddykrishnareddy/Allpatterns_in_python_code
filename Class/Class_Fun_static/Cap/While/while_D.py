    #D
class capital_alphabets:
    def __init__(self):
        pass
    def while_D(self,D):
        row=0
        while row<D:#6
            col =0
            while col<D:#6
                if (col==0 or col==1 and row!=1 and row!=2 and row!=3 and row!=4)or (col==2 and row!=1 and row!=2 and row!=3 and row!=4) or (col==3 and row!=0 and row!=2 and row!=3  and row!=5) or (col==4 and row!=0 and row!=1 and row!=4  and row!=5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()


