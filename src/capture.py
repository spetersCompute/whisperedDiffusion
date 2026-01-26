import readchar
import sounddevice as sd
import numpy
import threading

recording = False

def callback(indata, frames, time, status):
    if recording:
        print("Saving data:", indata)
    else:
        print("Ignoring data")

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
        input("Press Enter to stop\n")


if __name__ =="__main__":
    main()