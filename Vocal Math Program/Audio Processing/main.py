import speech_recognition as sr
from processing import processVoiceString



r = sr.Recognizer()

harvard = sr.AudioFile('Vocal Math Program/Audio Processing/temp3.wav')

with harvard as source:
    audio = r.record(source)

print(r.recognize_google(audio))


testString = "sine of x cosine of x tan of X tangent of X arc sine of Y Arc cosine of Y cosine inverse of Y arctan of y y equals plus or minus the √1 - x ^ 2"

processVoiceString(testString)

