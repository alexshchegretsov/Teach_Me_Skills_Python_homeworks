from random import randint as rd

A = [rd(-10, 10) for _ in range(10)]
print(A)
for i in range(1, len(A)):
    while i > 0 and A[i - 1] > A[i]:
        A[i - 1], A[i] = A[i], A[i - 1]
        i -= 1
print(A)
