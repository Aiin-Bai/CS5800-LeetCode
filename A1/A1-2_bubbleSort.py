def bubbleSort(A):
    n = len(A)
    for i in range(n):
        swapped = False  
        for j in range(n - 1 - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                swapped = True     
        if not swapped:
            break
    return A

# Sample test cases (Please add more test cases)
print(bubbleSort([-100, 13, 20]))  # returns [-100, 13, 20]
print(bubbleSort([13, -100, 20]))  # returns [-100, 13, 20]
print(bubbleSort([-100, 20, -10, 60, 80]))  # returns [-100, -10, 20, 60, 80]
print(bubbleSort([1, 2, 3, 4, -5]))  # returns [-5，1, 2, 3, 4]
print(bubbleSort([-1, -2, -3, -4, -5]))  # returns [-5，-4, -3, -2, -1]
