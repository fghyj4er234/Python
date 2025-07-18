#Write a function that takes a name as input and prints a greeting message.

"""
def greet(name):
    print("Hello",name)

print(greet("Umair"))

"""

#Write a function that takes two numbers and returns their sum
'''
def sum(a,b):
    sum = a + b
    return sum

print(sum(3,4))
'''
            

#Write a function to check if a number is even or odd.
'''
def even_odd_checker(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"    
result = even_odd_checker(9)
print("The number is :",result)
'''

#Write a function that returns the square and cube of a number.
'''
def sq_cub(n):
    sq = n*n
    cub = n*n*n
    return sq , cub

result = sq_cub(87)

print("Square and Cube of a number is :", result)
'''

#Write a function that takes a list of numbers and returns their average.
'''
def avg(numbers):
    if len(numbers) == 0:
        return 0
    total = sum(numbers)
    average = total/len(numbers)
    return average
my_list = [3,5,4,6,7]
result = avg(my_list)
print(result)'''

#Write a function that converts Celsius to Fahrenheit.
"""
def convert(C):
    F = (9/5)*C +  32
    return F
result = convert(37)
print(round(result))

"""

#Write a function that checks whether a number is prime or not
"""
def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(number ** 0.5) +1):  # Check up to square root of number
        if number % i == 0:
            return False
    return True
num = 15
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
"""
#Write a function that takes a string and returns the reversed string.
"""
def rev_strg(string):
    result= string[::-1]
    return result

str = "345789"
print(rev_strg(str))

    
"""

#Write a function that counts vowels in a string.
"""
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string :
      if char in vowels:
         count += 1
    return count

result = count_vowels("Hello , this is Umair.")
print("No of vowels in string are:",result)

"""

#Write a function that accepts marks of 3 subjects and returns grade based on average.
"""

def avg(s1,s2,s3):
    average = (s1+s2+s3)/3
    if average >= 90:
        return "Grade :A"
    elif average >= 80:
        return "Grade :B"
    elif average >= 70:
        return "Grade :C"
    elif average >= 60:
        return "Grade :D"
    else:
        return "Fail"
    
Ali = avg(90,90,75)
print(" Ali has got ",Ali)
    
"""

#Write a recursive function to calculate factorial of a number.
"""
def factorial(n):
    if n == 1 or n == 0:     # Base case: stop when n is 1 or 0
        return 1
    else:
        return n * factorial(n - 1)  # Recursive call
print("Factorial of 5 is:", factorial(5))

"""

#Write a recursive function to calculate the sum of first n natural numbers.
"""

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
print("sum of 1st 5 natural numbers is: " ,sum(5))

    """

#Write a recursive function to print the Fibonacci series up to n terms.
"""
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print Fibonacci series up to n terms
terms = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(terms):
    print(fibonacci(i), end=' ')
    """


#Write a recursive function to calculate the power of a number: base^exponent.
"""

def power(base,exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base,exponent-1)

print(power(4,4))
"""

#Write a recursive function to reverse a string.
"""
def reverse_string(s):
    if len(s) == 0:
        return ""  # Base case: empty string
    else:
        return s[-1] + reverse_string(s[:-1])  # Last char + reverse of the rest
print(reverse_string("hello"))

"""

