    #n
class small_alphabets:
    def __init__(self):
        pass
    def n(self,a):
        row=0
        while row<a:
            col=0
            while col<a:
                if (col==1 and row>0)or(row-col==0 and row<1) or (col==a-1 and row>0) or(row==0 and col<a-1 and col>1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
