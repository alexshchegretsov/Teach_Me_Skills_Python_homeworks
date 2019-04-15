def insert_sort(A):
    """Sorting list A by inserts"""
    for index in range(1, len(A)):
        while index > 0 and A[index-1] > A[index]:
            A[index-1], A[index] = A[index], A[index-1]
            index -= 1



def choice_sort(A):
    """Sorting list A by choice"""
    pass


def bubble_sort(A):
    """Sorting list A by bubble method"""
    pass


def test_sort(sorted_algorithm):
    print('Testing: ', sorted_algorithm.__doc__)
    print('testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sorted_algorithm(A)
    print('ok' if A == A_sorted else 'fail')

    print('testcase #2: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sorted_algorithm(A)
    print('ok' if A == A_sorted else 'fail')

    print('testcase #3: ', end='')
    A = [4, 2, 2, 4, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sorted_algorithm(A)
    print('ok' if A == A_sorted else 'fail')

    print('testcase #4: ', end='')
    A = []
    A_sorted = []
    sorted_algorithm(A)
    print('ok' if A == A_sorted else 'fail')

if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
