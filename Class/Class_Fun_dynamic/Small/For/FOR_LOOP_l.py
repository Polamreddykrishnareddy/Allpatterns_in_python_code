#l
class Small_alphabets:
    def __init__(self):
        pass
    def l(self,a):
        for row in range(a):
            for col in range(a):
                if( col==a//2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
