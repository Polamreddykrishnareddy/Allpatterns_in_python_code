#L
class capital_alphabets:
    def __init__(self):
        pass
    def L(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==0)or(row==a-1 and col!=a-1 and col!=a-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
