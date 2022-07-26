#S
class capital_alphabets:
    def __init__(self):
        pass
    def S(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0) or (row==col ) or (row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
