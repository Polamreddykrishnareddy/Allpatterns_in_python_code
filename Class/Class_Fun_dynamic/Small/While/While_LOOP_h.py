    #h
class small_alphabets:
    def __init__(self):
        pass
    def h(self,a):
        b=a+a
        row=0
        while row<b:
            col=0
            while col<a:
                if (col==0) or (row==b//2)or(col==a-1 and row>b//2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        
