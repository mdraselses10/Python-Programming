# Function to count the number of digits in the input string
s = input("Enter a string: ")

def count_digits(s):
    digit_count = 0
    for char in s:
        if char.isdigit():
            digit_count += 1
    return digit_count

print(f"Total digits are: {count_digits(s)}")
