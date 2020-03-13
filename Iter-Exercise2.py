counter = 0
sum = 0
largest_number = None
smallest_number = None

while True:
    numbers = input("Enter a number: ")

    if numbers == "done":
        break

    else:
        try:
            trynumbers = float(numbers)
            counter+= 1
            sum += trynumbers

            if largest_number is None:
                largest_number = trynumbers
            elif trynumbers > largest_number:
                largest_number = trynumbers

            if smallest_number is None:
                smallest_number = trynumbers
            elif trynumbers < smallest_number:
                smallest_number = trynumbers

        except:
            print("Invalid input")


print("Total: " + str(sum))
print("Count: " + str(counter))
print("Largest number: " + str(largest_number))
print("Smallest number: " + str(smallest_number))
