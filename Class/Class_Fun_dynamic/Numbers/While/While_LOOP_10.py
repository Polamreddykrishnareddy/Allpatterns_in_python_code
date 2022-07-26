#10
class Numbers:
    def __init__(self):
        pass
    def _10(self,a):
        b=a+3
        row=0
        while row<a+3:
            col=0
            while col<b:
                if (col==a//2)or(row==(a+2) and col<a)or(row+col==a//2)or(row==1 and col>b//2 and col<b-1)or(col==b-1 and row>1 and row<a) or(row==a and col>b//2 and col<b-1 )or(col==b//2 and row>1 and row<a):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
                col+=1
            row+=1
            print()
