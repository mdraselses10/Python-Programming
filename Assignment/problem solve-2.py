# Function to print the multiplication table of a number
n = int(input("Enter a number: "))

def print_multiplication_table(n):

    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_multiplication_table(n)
