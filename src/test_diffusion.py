from diffusion_client import DiffusionClient

client = DiffusionClient(device="cpu")
client.generate("A cyberpunk penguin hacking in a neon-lit alley", "test.png")