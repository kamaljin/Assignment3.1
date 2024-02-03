# Initialize an empty list to store numbers
numbers = []

# Ask the user to enter numbers until they enter an empty string
while True:
    num_input = input("Enter a number (press Enter to quit): ")

    # Check if the input is empty (user wants to quit)
    if num_input == "":
        break

    # Convert the input to a float and append it to the list
    try:
        number = float(num_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if there are numbers entered
if numbers:
    # Print the smallest and largest numbers
    print(f"The smallest number entered is: {min(numbers)}")
    print(f"The largest number entered is: {max(numbers)}")
else:
    print("No numbers entered.")
