import time
def stressan():
    A=input("Enter matrix A ")
    B=input("Enter matrix B ")
    t=time.clock()
    obj=""
    for i in A:
        for j in i:
            obj+=str(j)+" "
    a,b,c,d= (int(i) for i in obj.split())

    obj=""
    for i in B:
        for j in i:
            obj+=str(j)+" "
    e,f,g,h= (int(i) for i in obj.split())
    p1=a*(f-h)
    p2=(a+b)*h
    p3=(c+d)*e
    p4=d*(g-e)
    p5=(a+d)*(e+h)
    p6=(b-d)*(g+h)
    p7=(a-c)*(e+f)
    AB=[[p5+p4-p2+p6,p1+p2],[p3+p4, p1+p5-p3-p7]]
    for i in AB:
        for j in i:
            print j,
        print
    print "Time taken is "+str(time.clock()-t)

stressan()
