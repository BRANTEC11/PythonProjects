def time2sec(x):
    digit = [int(a) for a in str(x)]
    digit.reverse()
    total = 0
    i = 0
    multSec = 10
    multMin = 60
    while (i < len(digit)):
        if i == 0:
            total += digit[i]
        elif i == 1:
            total += (digit[i] * multSec)
        else:
            total += (digit[i] * multMin)
            multMin = multMin * 10
        i += 1
    print(total)
    return total

