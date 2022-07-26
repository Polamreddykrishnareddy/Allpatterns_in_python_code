    #Right symbol
class symbol:
    def __init__(self):
        pass
    def Right_symbol(self,a):
        print("Right symbol")
        for row in range(a):
            for col in range(a):
                if (row==a//2)or (col-row==a//2)or(col+row==a//2+a-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
