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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")