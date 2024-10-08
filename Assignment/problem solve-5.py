# Function to count the number of vowels in a string
s = input("Enter a string: ")

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(f"Number of vowels: {count_vowels(s)}")
