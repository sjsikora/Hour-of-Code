import sounddevice as sd
import soundfile as sf

def recordAudio():

    fs = 48000
      
    # seconds
    duration = 5
    myrecording = sd.rec(int(duration * fs), 
                         samplerate=fs, channels=2)
    sd.wait()
      
    # Save as FLAC file at correct sampling rate
    return sf.write('my_Audio_file.flac', myrecording, fs)
  