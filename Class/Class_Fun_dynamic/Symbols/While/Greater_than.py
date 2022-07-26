class symbols:
    def __init__(self):
        pass    
    print("Greater_than")
    def Greater_than(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if  (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()

