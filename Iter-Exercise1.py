counter = 0
sum = 0

while True:
    numbers = input("Enter a number: ")

    if numbers == "done":
        break

    else:
        try:
            trynumbers = float(numbers)
            counter+= 1
            sum += trynumbers
        except:
            print("Invalid input")

avg = sum/counter

print("Total: " + str(sum))
print("Count: " + str(counter))
print("Average: " + str(avg))
