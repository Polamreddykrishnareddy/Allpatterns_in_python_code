    #K
class capital_alphabets:
    def __init__(self):
        pass
    def for_K(self,K,k):
        for row in range(K):#8
            for col in range(k):#9
                if (col==0 or row==col+3)or (col==1 and row==3)or(row==2 and col==2)or (row==1 and col==3) or (row==0 and col==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


