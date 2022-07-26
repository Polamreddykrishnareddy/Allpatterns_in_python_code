class small_alphabits:
    def __init__(self):
        pass
    #a
    def for_a(self,a):
        for row in range(a):#10
            for col in range(a):#10
                if  (col==5 and row!=0 and row!=1) or(row==2 and col==2)or (row==1 and col==4) or (row==1 and col==3) or (row==5 and col==4) or (row==5 and col==3) or (row==6 and col==2) or (row==7 and col==2) or (row==8 and col==3)or (row==8 and col==4) or (row==9 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #b
    def for_b(self,b,B):
        for row in range(b):#11
            for col in range(B):#5
                if (col==0)or (row==6 and col==1)or (row==6 and col==2)or (row==6 and col==3)or (row==7 and col==4)or (row==8 and col==4)or (row==9 and col==4)or(row==10 and col==3)or(row==10 and col==2)or(row==10 and col==1) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #c
    def for_c(self,c):
        for row in range(c):#7
            for col in range(c):#7
                if  (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #d
    def for_d(self,d,D):
        for row in range(d):#10
            for col in range(D):#7
                if (col==6 and row!=9)or (row==9 and col!=6 and col!=0)or (row==5 and col!=0) or (row==6 and col==0)or (row==7 and col==0)or (row==8 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #e
    def for_e(self,e):
        for row in range(e):#7
            for col in range(e):#7
                if  (row==0 and col!=0) or (col==0 and row!=0 and row!=7 and row!=6)or (row==6 and col!=0) or (row==2 and col==1)or (row==2 and col==2)or (row==2 and col==5)or  (row==2 and col==3)or (row==2 and col==4)or (row==1 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        #f
    def for_f(self,f,F):
        for row in range(f):#9
            for col in range(F):#10
                if (col==4 and row!=0)or (row==0 and col==5)or (row==0 and col==6)or (row==0 and col==7)or (row==4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #g
    def for_g(self,g):
        for row in range(g):#10
            for col in range(g):#10
                if (col==9 and row!=0)or (row==9 and col==8)or (row==8 and col==7) or (row==0 and col==8)or (row==0 and col==7)or (row==0 and col==6)or (row==0 and col==5) or (row==1 and col==4)or (row==2 and col==4)or (row==3 and col==4)or (row==4 and col==5) or (row==4 and col==6) or (row==4 and col==7) or (row==4 and col==8):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #h
    def for_h(self,h,H):
        for row in range(h):# 11   
            for col in range(H):#10
                if (col==0) or (row==5 and col==1)or(row==5 and col==2)or(row==5 and col==3)or(row==5 and col==4)or(row==6 and col==5)or(row==7 and col==5)or(row==8 and col==5)or(row==9 and col==5)or(row==10 and col==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #i
    def for_i(self,i):
        for row in range(i):#10
            for col in range(i):#10
                if (col==5 and row!=1)or (col==6 and row!=1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #j
    def for_j(self,j):
        for row in range(j):#10
            for col in range(j):#10
                if (col==5 and row!=1)or (row==8 and col==4)or (row==7 and col==3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
        #k
    def for_k(self,k,K):
        for row in range(k):#15
            for col in range(K):#20
                if (col==0)or (row==col+8)or (row==8 and col==2)or (row==7 and col==3)or (row==6 and col==4)or (row==5 and col==5)or (row==4 and col==6) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #l
    def for_l(self,l):
        for row in range(l):#6
            for col in range(l):#6
                if col==4 or col==5:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


        #m
    def for_m(self,m,M):
        for row in range(m):#5
            for col in range(M):#10
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<M//2 and col>1)or (col==M//2 and row>0)or (row==0 and col>M//2 and col<M-1)or(col==M-1 and row>0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #n
    def for_n(self,n,N):
        for row in range(n):#5
            for col in range(N):#10
                if (col==1 and row>0)or(row-col==0 and row<1)or (row==0 and col<N//2 and col>1)or (col==N//2 and row>0)or (row==0 and col>N//2 and col<n):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #o
    def for_o(self,o):
        for row in range(o):#5
            for col in range(o):#5
                if (row==0 and col!=0 and col!=4) or (col==0 and row!=0 and row!=4) or (row==4 and col!=0 and col!=4) or (col==4 and row!=0 and row!=4):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #p
    def for_p(self,p,P):
        for row in range(p):#13
            for col in range(P):#6
                if (col==0 or row==0 and col!=5) or (row==1 and col==5)or (row==2 and col==5)or (row==3 and col==5)or (row==4 and col==5) or (row==5 and col!=5):#p
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #q
    def for_q(self,q,Q):
        for row in range(q):#13
            for col in range(Q):#8
                if (col==5 or row==0 and col!=0 and col!=6 and col!=7) or (row==1 and col==0)or (row==2 and col==0)or (row==3 and col==0)or (row==4 and col==0) or (row==5 and col!=0 and col!=6 and col!=7) or (row==11 and col==6) or (row==10 and col==7):#p
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #r
    def for_r(self,r):
        for row in range(r):#10
            for col in range(r):#10
                if (col==1 and row!=0 )or(row==0 and col==0) or (row==1 and col==2)or (row==1 and col==3)or (row==1 and col==4)or (row==1 and col==5) or (row==2 and col==6)or (row==3 and col==7):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #s
    def for_s(self,s,S):
        for row in range(s):#10
            for col in range(S):#7
                if (row==0 and col!=0 and col!=6) or (row==1 and col==0 or row==1 and col==6)or (row==2 and col==0)or (row==3 and col==1)or (row==4 and col==2)or (row==5 and col==3)or (row==6 and col==4)or (row==7 and col==5) or (row==8 and col==6)  or (row==9 and col!=0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #t
    def for_t(self,t):
        for row in range(t):#9
            for col in range(t):#9
                if (col==4) or (row==2) or (row==8 and col!=0 and col!=1 and col!=2 and col!=3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        #u
    def for_u(self,u):
        for row in range(u):#7
            for col in range(u):#7
                if (col==0 and row!=6) or (col==5  and row!=6 ) or (row==6 and col==1) or (row==6 and col==2) or (row==6 and col==3) or (row==6 and col==4)or(row==6 and col==6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #v
    def for_v(self,v,V):
        for row in range(v):#7
            for col in range(V):#15
                if (col+row==12) or (row==col):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        #w
    def for_w(self,w,W):
        for row in range(w):#7
            for col in range(W):#30
                if (col+row==12) or (row==col) or(col==row+12) or (col+row==24):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
        #x
    def for_x(self,x,X):
        for row in range(x):#10
            for col in range(X):#11
                if (col==row) or (row+col==9):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


    #y
    def for_y(self,y,Y):
        for row in range(y):#10
            for col in range(Y):#9
                if (row+col==8 ) or (row==0 and col==0) or (row==1 and col==1)or (row==2 and col==2)or (row==3 and col==3)or (row==4 and col==4) or (row==7 and col==0)or(row==6 and col==0):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

    #z
    def for_z(self,z):
        for row in range(z):#6
            for col in range(z):#6
                if (row==0) or (col+row==5) or (row==5):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

























