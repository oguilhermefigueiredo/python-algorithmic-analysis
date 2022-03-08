
# Calculating factorials using recursion
def log(n):
    if n <= 1:
        return 1

    return n*log(n-1)

print(log(5))

# Fibonacci sequence using recursion:
def f(n):
    if n <= 2:
        return 1

    return f(n-1) + f(n-2)

print(f(3))

# Check palidrome in any sequence of characters
def palindrome_checker(sequence):

    def chars(sequence):
        sequence = sequence.lower()
        ans = ''

        for char in sequence:
            if char in 'abcdefghijklmnopqrstuvxwyz1234567890':
                ans = ans + char

        return ans

    def check(sequence):
        if len(sequence) <= 1:
            return True

        else:
            return sequence[0] == sequence[-1] and check(sequence[1:-1])

    return check(chars(sequence))


print(palindrome_checker('2022 22 02'))
# OUTPUT: True
print(palindrome_checker("Madam, in Eden, I'm Adam"))
# OUTPUT: True

