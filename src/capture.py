import readchar
import sounddevice as sd
import numpy
import time
import threading
import soundfile as sf

recording = False
chunks = []
SAMPLE_RATE = 16000
#full_audio = numpy.concatenate(chunks, axis = 0)

def callback(indata, frames, time_info, status):
    global chunks
    if recording:
        chunks.append(indata.copy())
        print("Saving chunk", indata.shape)


def recordPrompt():
    global chunks
    chunks.clear()
    while not recording:
        time.sleep(0.02)
    while recording:
        time.sleep(0.02)    
    full_audio = numpy.concatenate(chunks, axis = 0)
    return full_audio, SAMPLE_RATE
 


def keyListener():
    global  recording 
    while True:
        key = readchar.readkey()
        if key == "r":
            recording = True
        elif key == "s":
            recording = False

