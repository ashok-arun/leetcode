import sys
def convert(s, numRows):
    ret=[""]*numRows
    ele=0
    if numRows==1:
        return s
    for i in range(len(s)):
        ret[ele]+=s[i]
        if int((i)/(numRows-1))%2==0:
            ele+=1
        else:
            ele-=1
    return "".join(ret)




print(convert(sys.argv[1], int(sys.argv[2])))
