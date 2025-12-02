def grid(f1,f2):
    f1()
    f2()
    f1()
    f2()
    f1()
def line1():
    print ('+','-'*4,'+','-'*4,'+')
def line2():
    print ('|',' '*4,'|',' '*4,'|')
def line3():
    line2()
    line2()
    line2()
grid(line1,line3)

