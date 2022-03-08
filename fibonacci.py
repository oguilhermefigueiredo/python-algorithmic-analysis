
# Functions to calculate a Fibonacci sequence given the value of an argument "n"

# Without recursion
def f(n):
    a, b = 0, 1

    for i in range(1, n):
        (a, b) = (b, a + b)

    return b

# With recursion
def f2(n):
    if n <= 2:
        return 1

    return f(n-1) + f(n-2)

#####
# Testing performance

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("f(34)", setup="from __main__ import f"))
# OUTPUT: 2.2140078649972565

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("f2(34)", setup="from __main__ import f2"))
# OUTPUT: 4.432545242016204
