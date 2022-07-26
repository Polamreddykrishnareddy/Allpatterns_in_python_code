#w
class Small_alphabets:
    def __init__(self):
        pass
    def w(self,a):
        b=a+2
        for row in range(b):
            for col in range(b):
                if (col==0) or (row-col==0 and row>a//2) or(col==b-1) or(row+col==b-1 and row>a//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        
