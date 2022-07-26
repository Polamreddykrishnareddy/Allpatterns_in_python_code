    #3
class Numbers:
    def __init__(self):
        pass
    def _3(self,a):
        b=a+a
        for row in range(b):
            for col in range(a):
                if (row==0 and col<a-1)or(row==b//2 and col<a-1)or(row==b-1 and col<a-1)or(col==a-1 and row!=a and row>0 and row<b-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
