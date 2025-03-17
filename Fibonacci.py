def fibonacci_iterative(n):
    a, b = 0, 1
    fib_series = []
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

n = int(input("Enter the number of terms: "))
print("Fibonacci Series:", fibonacci_iterative(n))
