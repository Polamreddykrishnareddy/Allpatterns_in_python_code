#Q
class capital_alphabets:
    def __init__(self):
        pass
    def for_Q(self,Q):
        for row in range(Q):#8
            for col in range(Q):#8
                if (col==1 and row==0)or (col==2 and row==0)or (col==3 and row==0)or (col==4 and row==1)or (col==4 and row==2)or (col==4 and row==3)or (col==5 and row==5)or (col==6 and row==6)or (col==1 and row==4)or (col==2 and row==4)or (col==3 and row==4)or (col==4 and row==4)or (col==0 and row==1)or (col==0 and row==2)or (col==0 and row==3)or (col==3 and row==3)or (col==2 and row==2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


