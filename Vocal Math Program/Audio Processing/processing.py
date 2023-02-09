from database import operationsDict, vaildSymbols, dictionary, opratorDict


testStringNew = "sine of x cosine of x tan of X tangent of X arc sine of Y Arc cosine of Y cosine inverse of Y arctan of y y equals plus or minus the √1 - x ^ 2"
testString = "negative e to the power of negative X 2 ^ x - 1 * caught of x times 0 ^ 0 Infinity to the power of 0 f Prime of x equals -7 * e ^ 4 + 5 * x ^ 2 F Prime of x equals -28 * x ^ 3 + 10x + 2 F Prime of x = 7 / 2 * the square root of x"


testString = "cosine of negative cosine of 2x"


expected = "-e^(-x) 2^x - 1 * cot(0)*0^0* inf^0 f'(x) = -7*e^4 + 5*x^2 f'(x) = -28*x^3 + 10x + 2 f'(x) = 7/2*sqrt(x)"

#Part of math functions are strings similar to "2x", "√1", "(", etc. This function will return true if the string is a math realted.
def filterKeyWord(word):

    if word.isnumeric():
        return True
    
    if len(word) == 1:
        return True

    if dictionary.check(word):
        return False

    #The idea here being, if there is very math related symbol i.e. √ then it will most likely only be math related.
    for char in word:
        if char in vaildSymbols:
            return True

    return False



def finalStringCleanup(string):
    wordArray = string.split(" ")
    opreators = opratorDict.values()
    operations = operationsDict.values()

    finalString = ""

    
    i = 0
    while(i < len(wordArray)):
        word = wordArray[i]


        if word in operations:
            finalString = word + "("

            j = 1
            notOperator = False
            while(notOperator):
                if wordArray[i + j] not in opreators:
                    notOperator = True
                else:
                    finalString += wordArray[i + j]
                    j += 1







def processVoiceString(voiceString):

    wordArray = voiceString.split(" ")
    oprartorKeys = opratorDict.keys()
    operationsKeys = operationsDict.keys()

    stringToReturn = ""
    lengthOfWordArray = len(wordArray)
    i = 0
    ofIndex = -1
    #Looping through every word...
    
    while(i < lengthOfWordArray):
        reachIndex = 0

        # Get the word to test
        word = wordArray[i].lower()
        wordAdded = False

        # If the word is of add a "(" to the string to return. Then ensure that the next token
        # is added, then add a ")" to the string to return. 
        #if word == "of":
        #    stringToReturn += "("
        #    ofIndex = i + 1

        # If the word is a number, or a letter, or a valid symbol, add it to the string to return.
        if filterKeyWord(word):

            stringToReturn += word
            wordAdded = True


        # If the word is not a number, letter, or valid symbol, then we need to test if it is a math related word and also
        # test if the word is the best fit. Sometime, the voice may pick up on "cosine inverse of.." the program, if going word by word,
        # the program will see cosine as cos, and inverse as nothing.
        else:
            wordToTest = word
            reachIndex, j = 0, 1
            reach = 5


            # Normally, the reach, or how far to look for the best word is five.
            # Yet, we need to adjust this based on where we are in the array.
            
            if (i + reach >= (len(wordArray) - 1)):
                reach = len(wordArray) - i

            while(j < reach):

                wordToTest += " " + wordArray[i + j]
                
                if ((wordToTest in oprartorKeys) or (wordToTest in operationsKeys)):
                    word = wordToTest
                    reachIndex = j

                j +=1

            if word in operationsKeys:
    
                word = operationsDict[word]
                stringToReturn += word
                wordAdded = True

            elif word in oprartorKeys:

                word = opratorDict[word]
                stringToReturn += word
                wordAdded = True



        ##if the word is an opreator, wait till add the paranthesis after the next keyword
        #if word in vaildSymbols:
        #    ofIndex = i + 2

        #if (i == ofIndex) and (wordAdded):
        #    stringToReturn += ")"

        if wordAdded:
            stringToReturn += " "

        i += 1 + reachIndex

    return stringToReturn









print(processVoiceString(testString))