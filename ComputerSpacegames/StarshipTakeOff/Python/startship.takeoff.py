# Import the 'os' and 'random' modules
import os
import random

# Define a function called 'successful_takeoff' that prints "GOOD TAKE OFF"
# and exits with a status code of 0
def successful_takeoff():
    print("GOOD TAKE OFF")
    exit(0)

# Clear the terminal screen
os.system("clear")

# Print a message indicating that the starship is taking off
print("STARSHIP TAKE-OFF")

# Generate random values for gravity (G) and weight (W)
G = random.randint(1, 20)
W = random.randint(1, 40)

# Calculate the required force (R) for takeoff
R = G * W

# Print the value of gravity and prompt the user to enter a force value
print("GRAVITY =", G)
print("TYPE IN FORCE (1-40)")

# Loop 10 times to allow the user to input a force value
for C in range(1, 10+1):
    F = int(input())   # Get the user's input as an integer
    if F > R:   # If the input force is greater than the required force
        print("TOO HIGH", end="")   # Print "TOO HIGH"
    elif F < R:   # If the input force is less than the required force
        print("TOO LOW", end="")   # Print "TOO LOW"
    else:   # If the input force is equal to the required force
        successful_takeoff()   # Call the 'successful_takeoff' function

    if C != 10:   # If this is not the last iteration of the loop
        print(", TRY AGAIN")   # Print ", TRY AGAIN" to prompt the user for another input

# Print a message indicating that the user has failed
print()
print("YOU FAILED!")
print("THE ALIENS GOT YOU")

# Exit the program with a status code of 1 to indicate failure
exit(1)
