import speech_recognition as sr


speechDict = {

    










    "plus": "+",
    "minus": "-",
    "slash": "/",
    "divided": "/",
    "times": "*",
    "multiplied": "*",



    "the power": "^",

    "bracket": "[",
    "Round brackets": "(",
    "parentheses": "(",
    "parenthesis": "(",

    "natural log": "ln",
    "cosine": "cos",
    "sign": "sin",
    "arcsign"
    


    "ex": "x",





}







r = sr.Recognizer()

harvard = sr.AudioFile('Vocal Math Program/Audio Processing/temp.wav')

with harvard as source:
    audio = r.record(source)

print(r.recognize_google(audio))