def grid(f1):
    f1()
    f1()



def line1():
    print ('+','-'*4,'+','-'*4,'+','-'*4,'+')
def line2():
    print ('|',' '*4,'|',' '*4,'|',' '*4,'|')
def square():
    line1()
    line2()
    line2()
    line2()
    line1()
grid(square)






