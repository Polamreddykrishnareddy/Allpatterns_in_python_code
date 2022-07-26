class symbols:
    def __init__(self):
        pass
    print("Diamond symbols")
    def Diamond_symbols(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if  (col-row==a//2)or(col+row==a//2+a-1)or(row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

