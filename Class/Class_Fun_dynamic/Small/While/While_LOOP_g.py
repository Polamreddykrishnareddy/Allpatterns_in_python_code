    #g
class small_alphabets:
    def __init__(self):
        pass
    def g(self,a):
        b=a+3
        row=0
        while row<b:
            col=0
            while col<a:
                if (col==a-1 ) or (row==0 and col>1) or(col==1 and row>0 and row<a//2)or(row==a//2 and col>1) or (row-col==3 and col>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        
