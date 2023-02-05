import speech_recognition as sr
from database import speechDict



r = sr.Recognizer()

harvard = sr.AudioFile('Vocal Math Program/Audio Processing/temp3.wav')

with harvard as source:
    audio = r.record(source)

print(r.recognize_google(audio))


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

for word in testStringArray:

    if word in mathWordsArray:
        stringToReturn += testSpeech[word]
