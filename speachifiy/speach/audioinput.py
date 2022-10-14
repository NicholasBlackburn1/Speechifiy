"""
this class is for handling taking mic input
"""
import audioop
import math
from multiprocessing import Process

import numpy as np
from utils import ConsoleLog as log
import pyaudio # Soundcard audio I/O access library
import wave # Python 3 module for reading / writing simple .wav files
import librosa
from IPython.display import Audio
import simpleaudio as sa
from utils import const
"""
need to get realtime audio processing working
"""

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



    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))
  
    P = Process(name="playsound",target=playy)

     # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                rate=RATE, input=True,input_device_index = 6,
                    frames_per_buffer=CHUNK)
    print ("recording started")


    
    # play and record loop 
    while const.voicetest == 1:

        # audio stream
        const.data = stream.read(CHUNK,exception_on_overflow = False)

        
        rms = audioop.rms(const.data, 2) + 0.001
        decibel = 20 * math.log(rms, 10)
        print(decibel)


        if(decibel >=-1.00 ):
           P.start() # Inititialize Process
        else:
            log.Warning("found sicelance")


    
    log.Warning("audio stream is done playing ")
    # Stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()


def playy():
    sa.play_buffer(const.data, 1, 2,sample_rate=44100)
