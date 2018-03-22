# Given a string, return the sum of the numbers appearing in the string, ignoring all other characters.
# A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) 
# tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)

def sumNumbers(letters):
    #code here
    sPos, ePos = -1, -1
    sumOfNum = 0
    for idx, l in enumerate(letters):
        if l.isdigit() == True:
            if sPos < 0:
                sPos = idx
                ePos = idx
            else:
                ePos = idx
        else:
            sumOfNum = add(letters, sumOfNum, sPos, ePos)
            sPos = -1

    sumOfNum = add(letters, sumOfNum, sPos, ePos)
    return sumOfNum

def add(letters, sum, sPos, ePos):
    if sPos >= 0:
        sum += int(letters[sPos:ePos+1])
    return sum

testData = ["abc123xyz", "aa11b33", "7 11", "34*f8s7"]
for t in testData:
    print(sumNumbers(t))