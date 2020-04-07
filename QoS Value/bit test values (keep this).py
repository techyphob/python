val = 0b11101001
print val
test = val & 192
test1 = val & 48
test2 = val & 12
test3 = val & 3
print test>>6
print test1>>4
print test2>>2
print test3

if test:
    print "thats how to do it"
