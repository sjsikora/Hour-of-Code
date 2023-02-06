from database import speechDict


testString = "sine of x cosine of x tan of X tangent of X arc sine of Y Arc cosine of Y cosine inverse of Y arctan of y y equals plus or minus the √1 - x ^ 2"



#Part of math functions are strings similar to "2x", "√1", "(", etc. This function will return true if the string is a math realted.
def filterRawString(word):
    if word.isnumeric():
        return True
    
    if len(word) == 1:
        return True
    
    return False


# Test if the word is the best fit. Sometime, the voice may pick up on "cosine inverse of.." the program, if going word by word,
# the program will see cosine as cos, and inverse as nothing.

def processVoiceString(voiceString):

    wordArray = voiceString.split(" ")
    speechDictKeys = speechDict.keys()

    stringToReturn = ""
    lengthOfWordArray = len(wordArray)
    i = 0
    #Looping through every word...
    while(i < lengthOfWordArray):

        # Get the word to test
        word = wordArray[i].lower()





        # If the word is a number, or a single character, then we can just add it to the string.
        if filterRawString(word):
            stringToReturn += word + " "
        else:
            # Normally, the reach, or how far to look for the best word is five.
            # Yet, we need to adjust this based on where we are in the array.
            reach = 5
            if (i + reach >= (len(wordArray) - 1)):
                reach = len(wordArray) - i

            wordToTest = word
            reachIndex, j = 0, 1

            while(j < reach):

                wordToTest += " " + wordArray[i + j]
                
                if (wordToTest in speechDictKeys):
                    word = wordToTest
                    reachIndex = j

                j +=1

            if word in speechDictKeys:
                stringToReturn += speechDict[word] + " "

        i += 1 + reachIndex

    return stringToReturn














print(processVoiceString(testString))