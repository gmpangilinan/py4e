def computepay(hours, rate):
    if float(hours) > 40:
        excess = float(hours) - 40
        extra = float(rate) * 1.5
        pay = (40*float(rate))+(excess*extra)

    else:
        pay = float(hours)*float(rate)

    return "Pay: " + str(pay)

hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

print(computepay(hours, rate))
