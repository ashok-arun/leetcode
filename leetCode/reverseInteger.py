import sys
def reverse(x):
    if x<0:
        ret="-"
        x=abs(x)
    else:
        ret=""
    y=str(x)
    for i in range(len(y)):
        ret+=y[len(y)-1-i]
    if int(ret)>2**31-1 or int(ret)<-2**31:
        return 0
    return int(ret)


# reverse a list list[::-1]

print(reverse(int(sys.argv[1])))
