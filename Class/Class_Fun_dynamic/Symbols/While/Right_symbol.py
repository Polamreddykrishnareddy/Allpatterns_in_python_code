class symbols:
    def __init__(self):
        pass    
    print("Right_symbol")
    def Right_symbol(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

