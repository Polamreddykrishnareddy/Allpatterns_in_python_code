#g
class Small_alphabets:
    def __init__(self):
        pass
    def g(self,a):
        b=a+3
        for row in range(b):
            for col in range(a):
                if (col==a-1 ) or (row==0 and col>1) or(col==1 and row>0 and row<a//2)or(row==a//2 and col>1) or (row-col==3 and col>a//2-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
