hours = input("Enter Hours: ")
try:
    tryhours = float(hours)
except:
    tryhours = -1

if tryhours < 0:
    print("Error, please enter numeric input")

else:
    rate = input("Enter Rate: ")
    try:
        tryrate = float(rate)
    except:
        tryrate = -1
    if tryrate < 0:
        print("Error, please enter numeric input")
    else:
        pay = float(hours)*float(rate)
        print("Pay: " + str(pay))
