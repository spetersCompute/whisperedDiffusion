from diffusers import StableDiffusionPipeline
import torch

class DiffusionClient:
    def __init__(self, model_name="stabilityai/sd-turbo", device="cpu"):
        """
        model_name: HuggingFace model repo
        device: "cpu" or "cuda"
        """
        print("Loading model...") 
        self.pipe = StableDiffusionPipeline.from_pretrained(model_name)
        print("Model loaded. Moving to device...")
        self.pipe = self.pipe.to(device)

    def generate(self, prompt, out_path="output.png"):
        """
        Generate an image form a text prompt.
        Return the path to the saved image.
        """
        try:
            image = self.pipe(prompt).images[0]
        except Exception as e:
            print(f"Error generating image: {e}")
            return None
        image.save(out_path)
        print(f"Saved to: {out_path}")
        return out_path