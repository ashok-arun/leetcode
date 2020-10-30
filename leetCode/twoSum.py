def twoSum(nums, target):
    check={}
    ret=[]
    for i in range(len(nums)):
        check[nums[i]]=i
    for i in range(len(nums)):
        if target-nums[i] in check and i!=check[target-nums[i]]:
            ret.append(i)
            ret.append(check[target-nums[i]])
            return ret
    return ret


print(twoSum([3,2,4],6))
        
