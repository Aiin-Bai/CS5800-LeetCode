def median2(X, Y):
### Write Your Code Here ###
    if len(X) > len(Y):
        X, Y = Y, X
    m, n = len(X), len(Y)
    total = m + n
    half = total // 2

    left, right = 0, m
    while left <= right:
        i = (left + right) // 2  
        j = half - i          

        leftX = X[i-1] if i > 0 else float('-inf')
        rightX = X[i] if i < m else float('inf')
        leftY = Y[j-1] if j > 0 else float('-inf')
        rightY = Y[j] if j < n else float('inf')

       
        if leftX <= rightY and leftY <= rightX:
            if total % 2:  
                return float(min(rightX, rightY))
            else:          
                return (max(leftX, leftY) + min(rightX, rightY)) / 2.0
        elif leftX > rightY:
            right = i - 1
        else:
            left = i + 1
print(median2([1], [2, 3])) # return 2.0
print(median2([1, 3], [2])) # return 2.0
print(median2([1, 2], [3, 4])) # returns 2.5
print(median2([1,2,3,4], [3,4])) # returns 3.0
print(median2([0,0,0,2,2], [1,1,1,1,1])) # returns 1.0
print(median2([1,3,5,7,9], [2,4,6,8,10,11])) # returns 6.0
print(median2([1,3,7,8,9], [2,4,5,6,10,11])) # returns 6.0
print(median2([1], [2,3,4,5,6,7])) # returns 4.0
print(median2([10,20,30,100], [40,60])) # returns 35.0

print(median2([1,1,1,1], [1,1,1,1])) # returns 1.0
print(median2([1], [4])) # returns 2.5
print(median2([1,2,3,3], [4])) # returns 3.0