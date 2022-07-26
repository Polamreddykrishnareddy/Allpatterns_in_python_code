
#m
class Small_alphabets:
    def __init__(self):
        pass
    def m(self,a):
        b=a+a
        for row in range(a):
            for col in range(b):
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<b//2 and col>1)or (col==b//2 and row>0)or (row==0 and col>b//2 and col<b-1)or(col==b-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
