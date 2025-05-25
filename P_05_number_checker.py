# ASk the user for width and loop until they enter a
# number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))
            # check the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)
