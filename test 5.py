num1=10
num2=20
num3=30
if(num1>=num2) and (num1>=num3):
    largest=num1
elif(num2>=num1) and (num2>=num3):
    largest=num2
else:
    largest=num3
print("the largest numbers between",num1,',',num2,',','and',num3,"is",largest) 
