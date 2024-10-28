def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Test the function
for i in range(10):
    print(f"F({i}) = {fibonacci_iterative(i)}")
import time

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Test both functions and compare their execution times
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")
def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1

# Test the generator
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized function
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance with the original recursive function
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

def fibonacci_list(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list[:n]

# Exercise 1
n = 10
fib_numbers = fibonacci_list(n)
print(f"Fibonacci sequence up to {n}: {fib_numbers}")

# Exercise 2
def first_fib_exceeding(value):
    if value < 0:
        return None  # There are no Fibonacci numbers less than 0

    fib_list = [0, 1]
    index = 1

    while fib_list[-1] <= value:
        fib_list.append(fib_list[-1] + fib_list[-2])
        index += 1

    return index

# excersise 3
import math

def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x

def is_fibonacci(n):
    if n < 0:
        return False
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Example usage:
number = 125
if is_fibonacci(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is not a Fibonacci number.")

#excersie 4
def fibonacci(n):
    """Generate Fibonacci numbers up to the nth term."""
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def fibonacci_ratios(n):
    """Calculate the ratios of consecutive Fibonacci numbers and observe convergence to the golden ratio."""
    fib_sequence = fibonacci(n)
    ratios = []
    
    for i in range(2, n):
        ratio = fib_sequence[i] / fib_sequence[i - 1]
        ratios.append(ratio)
    
    return ratios

# Example usage:
n_terms = 20
ratios = fibonacci_ratios(n_terms)
golden_ratio = (1 + 5 ** 0.5) / 2

print("Ratios of consecutive Fibonacci numbers:")
for i, ratio in enumerate(ratios, start=2):
    print(f"Fibonacci({i}) / Fibonacci({i-1}) = {ratio:.6f}")

print(f"\nGolden Ratio: {golden_ratio:.6f}")
