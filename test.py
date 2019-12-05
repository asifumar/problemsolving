import pdb
s = 'abc'

for i, a in enumerate(s):
    for j, b in enumerate(s[::-1]):
        print(i," ",j)
        print(s[i:j+1])
        pdb.set_trace()
        #print(s[i])