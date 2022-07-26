    #w
class small_alphabets:
    def __init__(self):
        pass
    def w(self,a):
        b=a+2
        row=0
        while row<b:
            col=0
            while col<b:
                if (col==0) or (row-col==0 and row>a//2) or(col==b-1) or(row+col==b-1 and row>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        
