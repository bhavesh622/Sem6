def initialize():
    m=[]
    r=int(input("Input number of rows"))
    c=int(input("Input number of columns"))
    while len(m)<r:
        m.append([])
        while len(m[-1])<c:
            m[-1].append(0)
    return m

def zeromat(r,c):
    m=[]
    while len(m)<r:
        m.append([])
        while len(m[-1]<c):
            m[-1].append(0)
    return m

# def copy(m)


def printmat(m):
    for rows in m:
        print([x for x in rows])

#  def add(m1,m2):
#     rowsm1= len(m1)
#     rowsm2= len(m2)
#     colsm1= len(m1[0])
#     colsm2= len(m2[0])
#     if rowsm1!=rowsm2 or colsm1!=colsm2:
#         print('Error adding, not the same sized matrices')
#     else:
#         m3= zeromat(rowsm1,colsm2)
#         for i in range(rowsm1):
#             for j in range(colsm2):
#                 m3[i][j] 


