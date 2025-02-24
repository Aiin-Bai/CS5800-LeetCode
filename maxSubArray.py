def maxSubArray(A:list):
## complete this function ##
    curSum = A[0]
    maxSum = A[0]
    start = 0
    tmpStart = 0
    end = 0
    for index, val  in enumerate(A[1:],start=1):
        if val> curSum+val:
            curSum = val
            tmpStart = index
        else:
            curSum+=val

        if curSum> maxSum:
            maxSum = curSum
            start = tmpStart
            end = index

    return A[start:end+1], maxSum

print(maxSubArray([-100])) # returns ([-100], -100)
print(maxSubArray([13, -100, 20]) )# returns ([20], 20)
print(maxSubArray([-100, 20, -10, 60, 80])) # returns ([20, -10, 60, 80], 150)
print(maxSubArray([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]))
# returns ([18, 20, -7, 12], 43)
print(maxSubArray([1,2,3,-500000,1]))
#return ([1,2,3])
