    #6
class numbers:
    def __init__(self):
        pass
    def for_6(self,a,b):
        for row  in range(a):#8
            for col in range(b):#6
                if (col==0 and row!=7 and row!=0 and row!=1) or (row==0 and col==2) or(row==1 and col==1)or (row==7 and col==1)or (row==7 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==4)or (row==4 and col==3) or (row==4 and col==1) or (row==4 and col==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


