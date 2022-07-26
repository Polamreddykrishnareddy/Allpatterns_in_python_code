#H
def while_H(H,h):
    row=0
    while row<H:#7
        col =0
        while col<h:#6
            if col==0 or col==5 or row==3  :
                print("*",end=" ")
            else:
                print(" ",end=" ")
            col +=1
        row +=1
        print()


