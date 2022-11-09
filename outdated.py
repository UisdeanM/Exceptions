months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# UNFINISHED
    

# slice month out of string
rawdate = input("Whats the date:")

splitdate = rawdate.split()

while True:
    try:
        rawdate = input("Whats the date:")
        splitdate = rawdate.split()
        if splitdate[0] in months:
            print("test3")
        else:
            continue


    except (ValueError, TypeError):
        print("test2")
        pass
    else:
        continue





print(f"{splitdate[0]}")
# index list for month

# if month in list, pass. if not in list, ValueError