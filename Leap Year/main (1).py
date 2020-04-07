def isYearLeap(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0: leap = False
        else: leap = True
    else: leap = False
    return leap
    
def daysInMonth(year, month):
    months30 = [4,6,9,11]
    if month == 2:
        if isYearLeap(year): return 29
        else: return 28
    elif month in months30: return 30
    else: return 31

def dayOfYear(year, month, day):
    days = 0
    for m in range(1,month):
        days += daysInMonth(year, m)
    return days + day

print(dayOfYear(2000, 12, 31))