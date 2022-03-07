
# Function to calculate a Fibonacci sequence given the value of an argument "n"
# It returns the result, and if you need to see the entire sequence, just
# uncomment the print line to see the whole sequence.
# This was my first program written in Python, but at first I have to declare
# three different variables, one for a, one for b and other one for the sum of a
# and b, but you can do the same operation declaring both initial values at the
# same time and do the replacement at the same expression.

def f(n):
    a, b = 0, 1

    for i in range(1, n):
        (a, b) = (b, a + b)

    return b

print(f(12))
# OUTPUT: 144
