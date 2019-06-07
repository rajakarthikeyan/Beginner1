import sys, string, math
a,b = input().split()
m = len(a)
n = len(b)
if n > m :
    i = 0
    while i<m1 and a[i] == n[i] :
        i += 1
    print(n-i)
elif n == m :
    i = 0
    while i<m and a[i] == b[i] :
        i += 1
    print(n-i)
else :
    i = 0
    while i<n and a[i] == b[i] :
        i += 1
    A = a[i:]
    B = b[i:]
    J = list(A)
    k = 0
    for w in s32 :
        if w in J :
            k += 1
            J.remove(w)
    print(m-i-k)
