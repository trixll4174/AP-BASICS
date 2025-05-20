# ASk the user for width and loop until they enter a
# number that is more than zero
error = "Please enter a number that is more than zero"
while True:

    try:
        # ask the user for a number
        width = float(input("Width: "))
        # check the number is more than zero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)