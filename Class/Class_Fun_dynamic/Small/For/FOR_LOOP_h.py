#h
class Small_alphabets:
    def __init__(self):
        pass
    def h(self,a):
        b=a+a
        for row in range(b):
            for col in range(a):
                if (col==0) or (row==b//2)or(col==a-1 and row>b//2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
