    #i
class small_alphabits:
    def __init__(self):
        pass
    def for_i(self,i):
        for row in range(i):#10
            for col in range(i):#10
                if (col==5 and row!=1)or (col==6 and row!=1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


