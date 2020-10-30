import sys
def myAtoi(s):
    ints=["0","1","2","3","4","5","6","7","8","9"]
    check=[" ", "+", "-"]
    ret=""
    for num in s:
        if len(ret)==0 and num not in check and num not in ints:
            return 0
        if num not in ints and len(ret)>0:
            break
        if num == "-" or num == "+" or num in ints:
            ret+=num
    if len(ret)==0 or ret=="+" or ret=="-":
        return 0
    if int(ret)<(-2)**31:
        return (-2)**31
    if int(ret)>2**31-1:
        return 2**31-1
    return int(ret)
        


print(myAtoi(sys.argv[1]))
