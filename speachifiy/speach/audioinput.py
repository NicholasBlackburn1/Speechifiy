"""
this class is for handling taking mic input
"""
from utils import ConsoleLog as log
import speech_recognition as s_r

# gets the voice from mic 
def getvoice():
    log.Debug(" pyaudio version"+ str(s_r.__version__))
