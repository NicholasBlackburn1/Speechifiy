"""
this class is for handling taking mic input
"""
from utils import ConsoleLog as log
import pyaudio # Soundcard audio I/O access library
import wave # Python 3 module for reading / writing simple .wav files
import librosa

# Setup channel info
FORMAT = pyaudio.paInt16 # data type formate
CHANNELS = 2 # Adjust to your number of channels
RATE = 44100 # Sample Rate
CHUNK = 1024 # Block Size
RECORD_SECONDS = 5 # Record time
WAVE_OUTPUT_FILENAME = "file.wav"

# Startup pyaudio instance
audio = pyaudio.PyAudio()

# gets the voice from mic to slow it down 
def getvoice():
    log.Warning("starting audio collection....")

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK,input_device_index=1)
    log.Debug(" recording...")
    frames = []

    # Record for RECORD_SECONDS
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    
    log.Debug(" Done recording...")


    # Stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    log.Warning("Creating wav file ....")
    # Write your new .wav file with built in Python 3 Wave module
    waveFile = wave.open("test.wav", 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    log.PipeLine_Ok("created audio file...")

    # should be output of ptich
    log.Warning("chaning pitch of file")

    y, sr = librosa.load('your_file.wav', sr=16000)
    y_third = librosa.effects.pitch_shift(y, sr=sr, n_steps=4)
    
    log.PipeLine_Ok("changed output pitch ....")
    
    # should save output file
    log.Warning("saving output file....")
    
    librosa.output.write_wav("unreadable.wav", y_third,sr)

    log.PipeLine_Ok("saved output file....")

    log.Warning("playing audio file")
    