    #i
class small_alphabets:
    def __init__(self):
        pass
    def i(self,a):
        b=a+3
        row=0
        while row<b:
            col=0
            while col<a+1:
                if (col==a//2 and row>1)or (row==b-1) or(col==a//2+1 and row>1) or(row==0 and col>a//2-1 and col<a-1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
        
