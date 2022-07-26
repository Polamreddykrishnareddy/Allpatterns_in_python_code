#Q
class capital_alphabets:
    def __init__(self):
        pass
    def Q(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0 and col!=0 and col!=a-2 and col!=a-1) or (row==a-2 and col!=0 and col!=a-1) or (col==0  and row!=0 and row<a-2) or (col==a-2 and row!=0 and row!=a-1)or (row==a-3 and col==a-3 ) or(row==a-4 and col==a-4)or(row==a-1 and col==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
