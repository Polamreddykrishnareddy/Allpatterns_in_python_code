#1
class Numbers:
    def __init__(self):
        pass
    def _1(self,a):
        row=0
        while row<a+2:
            col=0
            while col<a:
                if (col==a//2)or(row==a+1)or(row+col==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
