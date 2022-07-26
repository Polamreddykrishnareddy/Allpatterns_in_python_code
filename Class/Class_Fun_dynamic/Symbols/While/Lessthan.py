class symbols:
    def __init__(self):
        pass    
    print("Less-than")
    def Lessthan(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (row-col==a//2)or(col+row==a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

