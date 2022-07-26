#k
class small_alphabits:
    def _-init__(self):
        pass
    def while_k(self,k,K):
        row=0
        while row<k:#15
            col =0
            while col<K:#20
                if (col==0)or (row==col+8)or (row==8 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==5)or (row==4 and col==6) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
