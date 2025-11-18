class calculator:
    def __init__(s):
        s.a=float(input("Enter 1st Number"))
        s.b=float(input("Enter 2nd Number"))

    def sum(s):
        s.c=s.a+s.b
        return s.c
    def sub(s):
        s.c=s.a-s.b
        return s.c
    def mul(s):
        s.c=s.a*s.b
        return s.c
    def div(s):
        s.c=s.a/s.b
        return s.c

c=calculator()
while(True):
    i=int(input("""   
                      Enter 1 for sum.
                      Enter 2 for sub.
                      Enter 3 for mul.
                      Enter 4 for div.
                      Enter 0 for exit.
                    """))
    if(i==1):
        print("output",c.sum())
    elif(i==2):
        print("output",c.sub())
    elif(i==3):
        print("output",c.mul())
    elif(i==4):
        print("output",c.div())
    elif(i==0):
        print("Thanks")
        break
    else:
        print("wrong input")

    