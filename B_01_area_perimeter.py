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


# main routine starts here...

keep_going = ""
while keep_going == "":
    # get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")
    # calculATE area and perimeter
    area = width * height
    perimeter = 2 * (width + height)
    # display output
    print(f"Area: {area} units")
    print(f"Perimeter: {perimeter} units")
    # ask user if they want to keep going
    print()
    keep_going = input("Press enter to keep going or any key to quit")

print("Thank you for using the area / perimeter calculator.")
