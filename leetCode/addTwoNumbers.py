import sys
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    a=""
    b=""
    while l1:
        a+=str(l1.val)
        l1=l1.next
    while l2:
        b+=str(l2.val)
        l2=l2.next
    a=a[::-1]
    b=b[::-1]
    c=str(int(a)+int(b))[::-1]
    print(c)
    ret = ListNode()
    p=ret
    for i in range(len(c)):
        p.val=int(c[i])
        if i!=len(c)-1:
            p.next=ListNode()
            p=p.next
    return ret


def listToLink(a):
    ret = ListNode()
    p=ret
    for item in a:
        p.val=int(item)
        if item!=a[-1]:
            p.next=ListNode()
            p=p.next
    printLink(ret)
    return ret

def printLink(a):
    ret=""
    while a:
        ret+=str(a.val)
        a=a.next
        if a:
            ret+="->"
    print(ret)
        

printLink(addTwoNumbers(listToLink([8,6]),listToLink([6,4,9])))

