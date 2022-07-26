    #5
class Numbers:
    def __init__(self):
        pass
    def _5(self,a):
        b=a+a
        row=0
        while row<b:
            col=0
            while col<a:
                if (row==0)or(col==0 and row<a-1)or(row==a-1 and col<a-1)or(col==a-1 and row>a-1 and row<b-1)or(row==b-1 and col<a-1):#5
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        
