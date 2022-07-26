# v
class Small_alphabets:
    def __init__(self):
        pass
    def v(self,a):
        for row in range(a):
            for col in range(a):
                if (row+col==a-1 and row<a//2+1)or(row-col==0 and row<a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
