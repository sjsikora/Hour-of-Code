from database import speechDict, vaildSymbols, dictionary


testString = "sine of x cosine of x tan of X tangent of X arc sine of Y Arc cosine of Y cosine inverse of Y arctan of y y equals plus or minus the √1 - x ^ 2"


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


def processVoiceString(voiceString):

    wordArray = voiceString.split(" ")
    speechDictKeys = speechDict.keys()

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

        if word == "√1":
            pass

        # If the word is of add a "(" to the string to return. Then ensure that the next token
        # is added, then add a ")" to the string to return. 
        if word == "of":
            stringToReturn += "("
            ofIndex = i + 1

        # If the word is a number, or a letter, or a valid symbol, add it to the string to return.
        elif filterKeyWord(word):
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
                
                if (wordToTest in speechDictKeys):
                    word = wordToTest
                    reachIndex = j

                j +=1

            if word in speechDictKeys:
                stringToReturn += speechDict[word]
                wordAdded = True

        if (i == ofIndex) and (wordAdded):
            stringToReturn += ")"

        if wordAdded:
            stringToReturn += " "

        i += 1 + reachIndex

    return stringToReturn









print(processVoiceString(testString))