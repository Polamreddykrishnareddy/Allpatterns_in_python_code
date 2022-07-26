#V
class capital_alphabets:
    def __init__(self):
        pass
    def V(self,a):
        row=0
        while row<a:
            col=0
            while col<a+a:
                if (row==col)or(row+col==a+a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
