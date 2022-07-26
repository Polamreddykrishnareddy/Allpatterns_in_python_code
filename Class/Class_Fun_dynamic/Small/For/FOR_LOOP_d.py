#d
class Small_alphabets:
    def __init__(self):
        pass
    def d(self,a):
        b=a+a
        for row in range(b):
            for col in range(a):
                if (row==b//2 and col>0)or(col==0 and row>a and row<b-1) or(row==b-1 and col>0)or col==a-1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
