def zodiac(y):
    baseCase = ["null","Rooster","Dog","Pig","Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Sheep","Monkey"]
    revCase = ["null","Monkey","Sheep","Horse","Snake","Dragon","Rabbit","Tiger","Ox","Rat","Pig","Dog","Rooster"]
    if y == 0:
        print("Invalid Input")
    elif y < 0:
        y = abs(y)
        while (y-12) > 0:
            y = y - 12
        print("Year of the " + revCase[y])
    else:
        while (y-12) > 0:
            y = y - 12
        print("Year of the " + baseCase[y])
    while (y-12) > 0:
        y = y - 12
