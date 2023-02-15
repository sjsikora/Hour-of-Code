import speech_recognition as sr
from processing import processVoiceString

r = sr.Recognizer()

voiceFile = sr.AudioFile('Vocal Math Program/Audio Processing/temp3.wav')

with voiceFile as source:
    audio = r.record(source)

string = r.recognize_google(audio)

print(processVoiceString(string))
