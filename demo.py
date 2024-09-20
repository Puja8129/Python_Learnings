def sex(age):
    
    if age %2 == 0:
        return "female"
    
    if age %2== 1:
        return "male"


if __name__=="__main__":
    age = int(input("enter"))
    c=sex(age)
    print(c)


# Sure, here are some Python questions involving factorial calculations:

# 1. **Basic Factorial Calculation:**
#    Write a Python function to compute the factorial of a non-negative integer using both an iterative approach and a recursive approach.

#    ```python
#    # Iterative approach
#    def factorial_iterative(n):
#        if n < 0:
#            raise ValueError("Factorial is not defined for negative numbers")
#        result = 1
#        for i in range(1, n + 1):
#            result *= i
#        return result

#    # Recursive approach
#    def factorial_recursive(n):
#        if n < 0:
#            raise ValueError("Factorial is not defined for negative numbers")
#        if n == 0 or n == 1:
#            return 1
#        else:
#            return n * factorial_recursive(n - 1)
#    ```

# 2. **Factorial of a List:**
#    Write a Python function that takes a list of non-negative integers and returns a list of their factorials.

#    ```python
#    def factorial_list(numbers):
#        return [factorial_iterative(n) for n in numbers]
#    ```

# 3. **Factorial of Large Numbers:**
#    How would you modify the factorial function to handle very large numbers efficiently? Consider using Python’s built-in `math` library.

#    ```python
#    import math

#    def factorial_large(n):
#        if n < 0:
#            raise ValueError("Factorial is not defined for negative numbers")
#        return math.factorial(n)
#    ```

# 4. **Factorial Using Lambda Function:**
#    Implement a lambda function to calculate the factorial of a number.

#    ```python
#    factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)
#    ```

# 5. **Check Factorial Calculation Time:**
#    Write a script to compare the time it takes to compute the factorial of a large number using the iterative approach versus the built-in `math.factorial` function.

#    ```python
#    import time
#    import math

#    def factorial_iterative(n):
#        result = 1
#        for i in range(1, n + 1):
#            result *= i
#        return result

#    number = 1000

#    # Time iterative factorial
#    start = time.time()
#    factorial_iterative(number)
#    end = time.time()
#    print(f"Iterative factorial took {end - start} seconds")

#    # Time math.factorial
#    start = time.time()
#    math.factorial(number)
#    end = time.time()
#    print(f"math.factorial took {end - start} seconds")
#    ```

# 6. **Factorial of Floating Point Numbers:**
#    How would you handle the factorial of a floating point number or non-integer value? Consider using the Gamma function for non-integer factorials.

#    ```python
#    import math

#    def gamma_factorial(n):
#        if n < 0:
#            raise ValueError("Factorial is not defined for negative numbers")
#        return math.gamma(n + 1)

#    # Example usage
#    print(gamma_factorial(5.5))  # Gamma function can be used for non-integer values
#    ```

# Feel free to adapt these questions to your specific needs or use them as a basis to create more advanced problems!