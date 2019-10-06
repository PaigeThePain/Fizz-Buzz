print("Welcome to Fizz Buzz\n")

number = int(input("Please enter a number to count up to."))

counter = 1

while counter <= number:
    if counter % 3 == 0 and counter % 5 == 0:
        print ("Fizz Buzz")
    elif counter % 3 == 0:
        print("Fizz")
    elif counter % 5 == 0:
        print("Buzz")
    else:
        print(counter)
    counter += 1