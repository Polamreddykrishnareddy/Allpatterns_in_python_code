#X
class capital_alphabets:
    def __init__(self):
        pass
    def X(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row+col==a-1) or (row==col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
