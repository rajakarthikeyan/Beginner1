from itertools import combinations
x,y=map(int,input().split())
A=len(str(x))
K=list(combinations(str(x),A-y))
K=(sorted(K))
r="".join(K[0])
print(r)
