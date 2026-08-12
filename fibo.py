# Fibonacci number module
def fib(n):
    """Write a fibonacci series upto n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return a fibonacci series upto n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

print("Printing _name_: ", _name_)

if _name_ == "_main_":
    import sys
    print("Printing sys.arg[0]: ", sys.argv[0])
    print("Printing sys.arg[1]: ", sys.argv[1])
    fib(int(sys.argv[1]))