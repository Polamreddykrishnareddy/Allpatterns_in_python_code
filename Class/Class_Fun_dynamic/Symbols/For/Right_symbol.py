    #Right symbol
class symbols:
    def __init__(self):
        pass
    print("Right symbol")
    def Right_symbol(self,a):
        for row in range(a):
            for col in range(a):
                if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
