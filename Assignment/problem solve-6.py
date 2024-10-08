# Function to calculate the GCD of two numbers
#GCD=Greatest Common Divisor
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(f"GCD of {a} and {b} is: {find_gcd(a, b)}")
