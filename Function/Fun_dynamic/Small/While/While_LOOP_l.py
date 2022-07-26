    #l
def l(a):
    row=0
    while row<a:
        col=0
        while col<a:
            if( col==a//2) :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col+=1
        row+=1
        print()
        