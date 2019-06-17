num=int(input("enter num:"))
rev=0
while(num>0):
                remind=num%10
                rev=(rev*10)+remind
                num=num//10
                print("rev of num is =%d" %rev)
