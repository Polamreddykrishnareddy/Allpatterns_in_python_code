#i
class small_alphabits:
    def _-init__(self):
        pass
    def while_i(self,i):
        row=0
        while row<i:#10
            col =0
            while col<i:#10
                if (col==5 and row!=1)or (col==6 and row!=1):

                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
