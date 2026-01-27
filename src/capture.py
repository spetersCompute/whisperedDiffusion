import readchar
import sounddevice as sd
import numpy
import time
import threading

recording = False
chunks = []
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
    return full_audio
 


def keyListener():
    global  recording 
    while True:
        key = readchar.readkey()
        if key == "r":
            recording = True
        elif key == "s":
            recording = False

def main():
    t = threading.Thread(target=keyListener, daemon=True)
    t.start()
    with sd.InputStream(callback=callback, channels=1, samplerate=16000):
        full_audio = recordPrompt()
        print(full_audio.shape)


if __name__ =="__main__":
    main()