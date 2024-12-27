import pandas as pd

wb = pd.read_excel("F23P1-M013-Group3.xlsx", dtype=str)  # Reads through imported Excel file
bins = list(wb["bin"])  # Stores all binary  values from Excel file into "bins"
chars = list(wb["char"])  # Stores all characters from Excel file into "chars"
try:
    i = chars.index("\\n")  # Since the character is represented as "\\n" in the chars list, we change
    chars[i] = "\n"  # it here to its actual value of "\n" if it can find "\\n"
except:
    print("\n was not found")
try:
    i = chars.index("<space>")  # If we put " " in an Excel file, it wouldn't work, so we put "<space>
    chars[i] = " "  # instead and here if it finds "<space>" in the chars list, it replaces it
except:  # with an actual space, " "
    print("<space> was not found")


# read in a string and return the corresponding binary value for the first "character" within
# the string and a new string that has that same "character" removed from the front.


def getBinVal(s: str):
    # characters can be len of 1, 2, or 3
    # evaluate len of 3 chars, then len of 2 chars, and len of 1 char.
    # Get first 3 chars from string s if the string has 3 chars.
    # tests if they are in character list c.
    if len(s) >= 3:
        s3 = s[0:3]
        for i in range(len(chars)):
            if chars[i] == s3:
                s = s[3:]
                binVal = bins[i]
                return binVal, s
    # Get first 2 chars from string s if the string has 2 chars.
    # tests if they are in character list c.
    if len(s) >= 2:
        s2 = s[0:2]
        for i in range(len(chars)):
            if chars[i] == s2:
                s = s[2:]
                binVal = bins[i]
                return binVal, s
    # tests for 1 char
    if len(s) >= 1:
        for i in range(len(chars)):
            if chars[i] == s[0]:
                if len(s) > 1:
                    s = s[1:]
                else:
                    s = ""
                binVal = bins[i]
                return binVal, s
    # if no char was found, returns blank str and bin val
    return "", ""





# This function reads in a string of binary values. It returns the first binary value in the string
# as well as the string minus that first binary value.



def getFirstBin(s: str):
    flag = s[0]

    # This is a short binary value.
    if flag == "0":
        # S = 5, So get the first 5 values in the string.
        binVal = s[0:5]
        s = s[5:]
    # This is a long binary value.
    else:
        # L = 7, So get the first 7 values in the string.
        binVal = s[0:7]
        s = s[7:]
    return binVal, s



# This function takes as input a binary value and returns the corresponding character for that binary
# value.



def getChar(s):
    try:
        i = bins.index(s)
        charVal = chars[i]
    except:
        charVal = ''

    return charVal



# binOutput reads in a text file and creates a new text file called
# "BinOutput.txt" that contains the binary codes for the given file
def binOutput(file):
    # This opens a file and reads in the values before closing it
    # which allows us to refer to it for future processes
    openf = open(file, 'r')
    readf = openf.read()
    # print(readf)
    openf.close()

    binStr = ""
    # This while loop uses the function from task 2 to convert the text
    # from the file into their respective binary values
    while readf != "":
        # print(binStr, '\n', readf) # for testing
        binVal, readf = getBinVal(readf)
        binStr = binStr + binVal
    # print(binStr) # for testing

    # This calculates how many bits will be needed to store the line of binary values
    numBits = len(binStr)
    binStr = str(numBits) + "." + binStr

    # This chunk of code creates a txt file which contains the all the binary values
    # along with the amount of bits needed to store it before closing the file
    openf = open("BinOutput.txt", "w+")
    openf.write(binStr)
    openf.close()
    # print(binStr) # for testing


# binOutput("allChars.txt")


# This function reads in a text file with binary files and creates a new file "TextOutput.txt"
# that contains the characters that correspond to the given file.
def decode(p1="BinOutput.txt"):  # takes a string value, defaults it to "BinOutput.txt"
    f = open(p1)  # opens the file
    s = f.read()  # reads the value in the files
    f.close()  # closes the file

    i = s.index(".")  # This finds the index where the period is in the binary value returned
    s = s[i + 1:]  # This makes s = the binary value found, after the index where the period is

    # Use the functions from Task 3 to create a list of binary values and
    # then go through that list of values to find the characters that go with
    # those codes.

    charStr = " "
    while s != " ":
        binval, s = getFirstBin(s)
        charStr = charStr + getChar(binval)

    # this code opens the text file, writes it out, then closes
    f = open("TextOutput", "w+")
    f.write(charStr)
    f = f.close

# two strings (files) as inputs within the function
def checkIdentical(input1="BinOutput.txt", input2="TextOutput.txt"):
    # opens the files into variables
    inputVar1 = open(input1)
    inputVar2 = open(input2)
    # reads the opened files into new variables
    s1 = inputVar1.read()
    s2 = inputVar2.read()
    # closes the files
    inputVar1.close()
    inputVar2.close()
    # checks to see if they are equal and returns true if so,
    # if not returns false
    if s1 == s2:
        return True
    else:
        return False


