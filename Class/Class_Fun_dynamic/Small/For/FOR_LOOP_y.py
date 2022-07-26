#y
class Small_alphabets:
    def __init__(self):
        pass
    def y(self,a):
        for row in range(a):
            for col in range(a):
                if (row-col==0 and col<a//2)or (row+col==a-1 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
