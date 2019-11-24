# The fibonacci sequence is defined as follows: Fibo(n) = Fibo(n-1) + Fibo(n-2)
# Where Fibo(0) = 0 and Fibo(1) = 1
# This leads to a sequence that grows as follows: 0,1,1,2,3,5,8,13,21... etc.
# Create a function that for any given integer n, returns the nth element of the fibonacci sequence.
# Do not edit the function name or arguments.

def Fibonacci(n):
    if n <= 1:
        return n;
    else:
        return(Fibonacci(n-1) + Fibonacci(n-2))


# Run or edit this code to test your function
print(Fibonacci(0))     #Should be 0
print(Fibonacci(1))     #Should be 1
print(Fibonacci(2))     #Should be 1
print(Fibonacci(10))    #Should be 55
