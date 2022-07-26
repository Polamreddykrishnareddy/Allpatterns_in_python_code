#z
class Small_alphabets:
    def __init__(self):
        pass
    def z(self,a):
        for row in range(a):
            for col in range(a):
                if (row==0 )or (row+col==a-1 ) or(row==a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
