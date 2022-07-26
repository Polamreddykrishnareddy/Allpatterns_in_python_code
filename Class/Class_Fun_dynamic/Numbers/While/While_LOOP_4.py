    #4
class Numbers:
    def __init__(self):
        pass
    def _4(self,a):
        row=0
        while row<a+2:
            col=0
            while col<a+1:
                if (col==a-1)or(row==a-1)or(row+col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
