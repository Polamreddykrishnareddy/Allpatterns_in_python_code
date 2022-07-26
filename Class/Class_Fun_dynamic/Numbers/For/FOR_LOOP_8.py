#8
class Numbers:
    def __init__(self):
        pass
    def _8(self,a):
        b=a+4
        for row in range(b):
            for col in range(a):
                if (row==0 and col>0 and col<a-1)or(row==b//2 and col>0 and col<a-1)or(row==b-1 and col>0 and col<a-1)or(col==0 and row!=b//2 and row>0 and row<b-1)or(col==a-1 and row!=b//2 and row<b-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
