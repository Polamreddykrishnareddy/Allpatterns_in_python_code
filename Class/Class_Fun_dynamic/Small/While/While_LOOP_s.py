    #s
class small_alphabets:
    def __init__(self):
        pass
    def s(self,a):
        b=a+a
        row=0
        while row<b:
            col=0
            while col<a:
                if  (row==0 and col>0) or (col==0 and row>0 and row<b//2-1) or(row==b//2-1 and col>0 and col<a-1) or(col==a-1 and row>a-1 and row<b-2)or(row==b-2 and col<a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
            
