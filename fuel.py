# x user input
# y user input
# output x/y as a %
# if <=1%, output E
# if >=99%, output F





#get x and y


#change fraction to percent

percent = 0

# 
while percent == 0:
    fraction = input("Fuel:")
    try:
        x = int(fraction[0])
        y = int(fraction[2])
    except (ValueError, ZeroDivisionError, AttributeError, NameError):
        pass
    else:
        if x <= y and len(fraction) == 3:  # 1.5/3 was giving out 20%. kinda hacky way of ensuring no fractions as input
            percent = round((x/y)*100)
            if 1 < percent < 99:
                print(f"{percent}%")
            elif percent <= 1:
                print("E")
            elif percent >= 99:
                print("F")
            break
        else:
            pass
    









