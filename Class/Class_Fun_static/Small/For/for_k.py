    #k
class small_alphabits:
    def __init__(self):
        pass
    def for_k(self,k,K):
        for row in range(k):#15
            for col in range(K):#20
                if (col==0)or (row==col+8)or (row==8 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==5)or (row==4 and col==6) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

