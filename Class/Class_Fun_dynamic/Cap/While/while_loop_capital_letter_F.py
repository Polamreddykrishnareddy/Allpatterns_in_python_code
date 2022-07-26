#F
class capital_alphabets:
    def __init__(self):
        pass
    def F(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col<a-2) or (row==a//2-1 and col<a-2)or(col==0 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
