hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

if float(hours) > 40:
    excess = float(hours) - 40
    extra = float(rate) * 1.5
    pay = (40*float(rate))+(excess*extra)

else:
    pay = float(hours)*float(rate)

print("Pay: " + str(pay))
