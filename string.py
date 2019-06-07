x=input()
x=int(x)
A=[]
for i in range(0,x):  
    w=input()
    A.append(w)
H=[]
for i in zip(*A):
    if i.count(i[0])==len(i): 
        H.append(i[0])
    else:
        break
print(''.join(H))
