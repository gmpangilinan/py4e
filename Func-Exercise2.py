def computegrade(score):
    try:
        tryscore = float(score)
    except:
        tryscore = -1


    if tryscore < 0:
        return "Bad Score"

    else:
        score = float(score)
        if score > 1.0:
            return "Bad score"
        elif score >= 0.9:
            return "A"
        elif score >= 0.8:
            return "B"
        elif score >= 0.7:
            return "C"
        elif score >= 0.6:
            return "D"
        elif score < 0.6:
            return "F"

score = input("Enter score: ")
print(computegrade(score))
