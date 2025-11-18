from faster_whisper import WhisperModel

class WhisperClient:
    def __init__(self, model_name="base.en", device="cpu", compute_type="int8"):
        """
        model_name: whisper model name or path
        device: "cpu" or "cuda"
        compute_type: "int8", "int16", or "float32"
        """

        self.model = WhisperModel(model_name, device=device, compute_type=compute_type)


    def transcribe(self, audio_path):
        """Transcribe audio and return the full text string."""
        segments, _ = self.model.transcribe(audio_path)
        transcript = " ".join([segment.text.strip() for segment in segments])
        return transcript

    
