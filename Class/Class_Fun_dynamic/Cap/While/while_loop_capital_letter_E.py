#E
class capital_alphabets:
    def __init__(self):
        pass
    def E(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==0) or (row==a//2 )or (row==a-1)or(col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
