from faster_whisper import WhisperModel

model = WhisperModel("base.en", device="cpu", compute_type="int8")
text, _ = model.transcribe("/home/stephenp/Documents/berkshireCNBC.wav")
print("".join([segment.text for segment in text]))