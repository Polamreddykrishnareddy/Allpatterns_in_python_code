#x
class small_alphabits:
    def _-init__(self):
        pass
    def while_x(self,x,X):
        row=0
        while row<x:#10
            col=0
            while col<X:#11
                if col==row or row+col==8:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col +=1
            row +=1
            print()
