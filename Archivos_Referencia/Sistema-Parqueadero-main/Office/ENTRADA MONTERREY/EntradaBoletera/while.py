# Define the list
nums = []

# The loop will run while the length of the
# list nums is less than 4
while len(nums) < 4:
    # Ask for user input and store it in a variable as an integer.
    user_input = int(input("Enter an integer: "))
    # If the input is an even number, add it to the list
    if user_input % 2 == 0:
        nums.append(user_input)
        print(nums)
