class Matrix:
    r,c=0,0
    m=[]
    def __init__(self,r,c,m):
        self.r=r
        self.c=c
        self.m=m
        while len(m) <r:
            m.append([])
            while len(m[-1])<c:
                m[-1].append(0.0)
        return m
    def printm(m):
        for row in m:
            print([x for x in row])
    # def add():
        # for i in m:
