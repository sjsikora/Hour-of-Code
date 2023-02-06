
testSpeech = {
    "sine": "sin",
    "arc sine": "arcsin",
    "sine inverse": "arcsin",

    "cosine": "cos",
    "arc cosine": "arccos",
    "cosine inverse": "arcos",

    "tan": "tan",
    "arc tan": "arctan",
    "tan inverse": "arctan",

    "tangent": "tan",
    "arc tangent": "arctan",
    "tan inverse": "arctan",
}


testString = "sine of x cosine of x tan of X tangent of X arc sine of Y Arc cosine of Y cosine inverse of Y arctan of y y equals plus or minus the √1 - x ^ 2"


testStringArray = testString.split(" ")
mathWordsArray = testSpeech.keys()

stringToReturn = ""
lengthOfWordArray = len(testStringArray)


i = 0
while(i < lengthOfWordArray):

    j = 0

    #if ((4 + i) >= lengthOfWordArray):
    #    j = lengthOfWordArray - i
    #else:
    #    j = 5

    word = testStringArray[i].lower()


    # Test if the word is the best fit. Sometime, the voice may pick up on "cosine inverse of.." the program, if going word by word,
    # the program will see cosine as cos, and inverse as nothing.
    wordToTest = word
    reachIndex, j = 1, 1
    while(j < 5):

        #Error, should adjust index based on the end of the sentence, not just break.
        if (i + j >= len(testStringArray)):
            break

        wordToTest += " " + testStringArray[i + j]

        if (wordToTest in mathWordsArray):
            word = wordToTest
            reachIndex = j

        j +=1


    if word in mathWordsArray:
        stringToReturn += testSpeech[word] + " "


    i += 1 + (reachIndex - 1)





print(stringToReturn)