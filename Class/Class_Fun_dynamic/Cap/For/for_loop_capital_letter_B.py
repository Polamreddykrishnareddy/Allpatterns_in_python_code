#B
class capital_alphabets:
    def __init__(self):
        pass
    def B(self,b):
        for row in range(b):
            for col in range(b):
                if (col==0)or(row==0 and 2<b and col!=b-1 and col!=b-2)or(row==b-1 and 2<b and col!=b-1 and col!=b-2)or(col==b-2 and row!=0 and row!=b-1 and row!=b//2)or(row==b//2 and col!=b-1 and col!=b-2 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
