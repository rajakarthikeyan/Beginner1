num=int(input("please enter any num:"))
count=0
while(num>0):
    num=num//10
    count=count+1
print("\n  number of digits in a given num=%d"%count)   
