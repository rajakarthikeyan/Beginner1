number=int(input("enter positive integer:"))
exponent=int(input("enter exponent value:"))
power=1
for i in range(1,exponent +1):
    power=power*number
print("the result of {0} power {1}={2}".format(number,exponent,power))
