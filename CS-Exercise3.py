score = input("Enter score: ")

try:
    tryscore = float(score)
except:
    tryscore = -1



if tryscore < 0:
    print("Bad score")

else:
    score = float(score)
    if score > 1.0:
        print("Bad score")
    elif score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    elif score < 0.6:
        print("F")
