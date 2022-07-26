    #w
class small_alphabits:
    def __init__(self):
        pass
    def for_w(self,w,W):
        for row in range(w):#7
            for col in range(W):#30
                if (col+row==12) or (row==col) or(col==row+12) or (col+row==24):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

