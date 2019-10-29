def is_leap(year):
    leap = False
    quo1, rem1 = divmod(year, 4)
    quo2, rem2 = divmod(year, 100)
    quo3, rem3 = divmod(year, 400)
    if rem1 == 0:
        if rem3 == 0 or rem2 != 0:
            leap = True
    else:
        leap = False

    return leap


year = int(input())
print(is_leap(year))
