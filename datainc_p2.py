count = 0

class path:
    

    def calcpath (self, m, n, d1, d2, d3, d4):

        global count
        
        if (d1 < 0 or d2 < 0 or d3 < 0 or d4 < 0 or d1 >= n or d2 >= n or d3 >=n or d4 >= n or m < 0) :
            return
        if (m==0):
            count=count+1
            return

        self.calcpath(m-1, n, d1+1, d2, d3, d4)
        self.calcpath(m-1, n, d1, d2+1, d3, d4)
        self.calcpath(m-1, n, d1, d2, d3+1, d4)
        self.calcpath(m-1, n, d1, d2, d3, d4+1)
        self.calcpath(m-1, n, d1-1, d2, d3, d4)
        self.calcpath(m-1, n, d1, d2-1, d3, d4)
        self.calcpath(m-1, n, d1, d2, d3-1, d4)
        self.calcpath(m-1, n, d1, d2, d3, d4-1)


test = path()
lst = []
for i in range(9):
    for j in range(9):
        for k in range(9):
            for l in range(9):
                test.calcpath(10, 10, i, j, k, l)
                lst.append(count)
                count=0

print(max(lst))
print(min(lst))
