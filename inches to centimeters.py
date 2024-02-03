# Define the conversion factor from inches to centimeters
INCHES_TO_CM = 2.54

# Prompt the user to enter the initial value in inches
print("Enter a length in inches (enter a negative value to quit):")

# Continuously prompt the user for input and convert inches to centimeters
while True:
    # Get user input as a float
    inches = float(input("Inches: "))

    # Check if the input is negative, if so, end the program
    if inches < 0:
        print("Program ended.")
        break

    # Convert inches to centimeters
    centimeters = inches * INCHES_TO_CM

    # Print the result
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")
