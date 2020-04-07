def FirstFactorial(num):
    if num - 1 > 0:
        return num * FirstFactorial(num-1)
    else:
        return num

#print (FirstFactorial(int(input())))

def LongestWord(sen):
    l_word = ""
    for w in sen.split(" "):
        if not w.isalpha():
            t = ""
            for i in range (0,len(w)):
                if w[i].isalpha() or w[i].isdigit():
                    t = t + w[i]
            w = t
        if len(w) > len(l_word):
            l_word = w
    return l_word


#print (LongestWord("123456789 98765432"))
#print (LongestWord(input()))

def LetterCapitalize(str):
    words = str.split(" ")
    for i in range (0,len(words)):
        words[i] = words[i][0].upper()+words[i][1:len(words[i])]
    return (' '.join(words))


# keep this function call here  
#print (LetterCapitalize("the test input goes here"))

def SimpleSymbols(s):
    for i in range (0,len(s)):
        if s[i].isalpha():
            if i==0 or i== (len(s)-1): return "false"
            elif not(s[i-1]=="+" and s[i+1]=="+"): return "false"
    return "true"
#print (SimpleSymbols("+d===+a+"))

def AlphabetSoup_o(str): 
    str = list(str)
    for i in range (0,len(str)-1):
        low = str[i]
        for j in range (i,len(str)):
            if str[j] < low:
                low = str[j]
                str[j] = str[i]
                str[i] = low    
    return ''.join(str)
def AlphabetSoup(s): 
    return ''.join(sorted(list(s)))
#print (AlphabetSoup("hello"))

def NumberReverse(num):
    num = list(num)
    num_rev = ""
    for i in range (0,len(num)-1):
        low = num[i]
        for j in range (i,len(num)):
            if num[j] < low:
                low = num[j]
                num[j] = num[i]
                num[i] = low
    num = ''.join(num)
    num_rev = num[::-1]
    if int(num_rev) < int(num):
        result = int(num)-int(num_rev)
    else:
        result = int(num_rev)-int(num)
    return result

def KaprekarsConstant(num):
    count = 1
    answer = NumberReverse(num)
    while answer != 6174:
        answer = NumberReverse(format(answer,'04'))
        count += 1
        print (str(answer)+" "+str(count))
    return count
#6174
def KaprekarsConstanto(num): 
    count = 0
    while num != 6174:
        num = sorted(list('%04d' %num))
        x,y=int(''.join(num)),int(''.join(num[::-1]))
        num =  y-x
        count += 1
    return count

# keep this function call here  
#print (KaprekarsConstant("2111"))

def EightQueens(strArr): 
    for i in range(0,len(strArr)):
        for j in range(i+1,len(strArr)):
            if int(strArr[i][1]) == int(strArr[j][1]) or int(strArr[i][3]) == int(strArr[j][3]) or int(strArr[i][1])-int(strArr[j][1]) == int(strArr[j][3])-int(strArr[i][3]) or int(strArr[i][1])-int(strArr[j][1]) == int(strArr[i][3])-int(strArr[j][3]):
                return strArr[i]
    return 'true'
#print (EightQueens(["(1,1)", "(7,2)", "(4,3)", "(6,4)", "(8,5)", "(2,6)", "(5,7)", "(5,8)"]))

def PentagonalNumber(n): 
    return ((n * (n-1)/2)*5) + 1
#print (PentagonalNumber(5))
def ClosestEnemyII(strArr): 
    enemies,dist = [],[]
    width, height= len(strArr[0]),len(strArr)
    for i,row in enumerate(strArr):
        for j,col in enumerate(row):
            if col == '1': x,y = i,j
            if col == '2': enemies.append((i,j))
    if enemies:
        for e in enemies:
            dist.append(min(abs(e[0] - x), abs(width - (e[0]-x)))+min(abs(e[1] - y), abs(height -(e[1]-y))))
    else:
        dist.append(0)
    return min(dist)
import time
def factorial(num):
    fac = 1
    for i in range (1, num+1):
        fac = fac * i
    return fac
def fac(num):
    if num == 0:
        return 1
    return num * fac(num - 1)



def ChessboardTraveling(coords): 
    u, r  = int(coords[6]) - int(coords[1]), int(coords[8]) - int(coords[3])
    return factorial (u+r)/(factorial(u)*factorial(r))
#print (ChessboardTraveling("(1 1)(8 8)"))














