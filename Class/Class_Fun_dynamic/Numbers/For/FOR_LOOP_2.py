    #2
class Numbers:
    def __init__(self):
        pass
    def _2(self,a):
        b=a+2
        for row in range(b):
            for col in range(a):
                if (row==0 and col>1 and col<a-1)or(row==a//2+1 and col>1 and col<a-1)or(col==1 and row>0 and row<a//2+1)or(col==a-1 and row>0 and row<a//2+1)or(row+col==a+1)or(row==a+1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
