# Function to find the second largest number in a list

numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

def find_second_largest(numbers):

    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]

second_largest = find_second_largest(numbers)

if second_largest is not None:
    print(f"The second largest number is: {second_largest}")
else:
    print("The list doesn't have a second largest number.")
