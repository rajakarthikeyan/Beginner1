ch=input("please enter your own character")
if((ch>='a'and ch<='z') or (ch>='A' and ch<='Z')):
    print("the given character",ch,"is an alphabet")
elif(ch>='0' and ch<='9'):
    print("the given character",ch,"is an digit")
else :
    print("the given character",ch,"is not an alphabet or digit")
