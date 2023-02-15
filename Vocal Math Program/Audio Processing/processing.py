from database import operationsDict, vaildSymbols, dictionary, opratorDict

testString = "23305 * x cosine parentheses 3x and"


#Part of math functions are strings similar to "2x", "√1", "(", etc. This function will return true if the string is a math realted.
def filterKeyWord(word):

    if word.isnumeric():
        return True
    
    if len(word) == 1:
        return True

    if dictionary.check(word):
        return False

    #The idea here being, if there is very math related symbol i.e. √ then it will most likely only be math related.
    numbersOnly = False
    pastNumbersOnly = False
    for char in word:

        if pastNumbersOnly and char.isnumeric():
            return False

        if numbersOnly and (not char.isnumeric()):
            pastNumbersOnly = True

        if char.isnumeric():
            numbersOnly = True

        if char in vaildSymbols:
            return True

    return True





def finalStringCleanup(string):
    wordArray = string.split(" ")
    
    opreators = opratorDict.values()
    
    finalString = ""
    i = 0
    while(i < len(wordArray)):

        word = wordArray[i]

        if i == (len(wordArray) - 1):
            finalString += word
            return finalString


        if wordArray[i] in opreators:
            finalString += word + " "
        elif wordArray[i + 1] in opreators:
            finalString += word + " "
        else:
            finalString += "(" + word + ")"


        i += 1
    



def processVoiceString(voiceString):

    wordArray = voiceString.split(" ")
    oprartorKeys = opratorDict.keys()
    operationsKeys = operationsDict.keys()

    stringToReturn = ""
    lengthOfWordArray = len(wordArray)
    i = 0
    #Looping through every word...
    
    while(i < lengthOfWordArray):
        reachIndex = 0

        # Get the word to test
        word = wordArray[i].lower()
        wordAdded = False

        if word == "of":
            stringToReturn += "("

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

        if wordAdded:
            stringToReturn += " "

        i += 1 + reachIndex

    stringToReturn = finalStringCleanup(stringToReturn)

    return stringToReturn

print(processVoiceString(testString))