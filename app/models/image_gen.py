'''from diffusers import StableDiffusionPipeline
from PIL import Image

# Carregar o modelo ao iniciar o módulo
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cpu")  # Use "cuda" se tiver GPU

def generate_image(description: str) -> Image:
    """
    Gera uma imagem com base em uma descrição textual.

    Args:
        description (str): Descrição da imagem a ser gerada.

    Returns:
        Image: Objeto PIL contendo a imagem gerada.
    """
    if not description.strip():
        raise ValueError("A descrição não pode estar vazia.")
    
    result = pipe(description).images[0]
    return result'''
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
from PIL import Image
import torch

# Configuração do modelo
model_id = "CompVis/stable-diffusion-v1-4"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    scheduler=scheduler,
    torch_dtype=torch.float32
).to("cpu")  # Força o uso da CPU

pipe.enable_attention_slicing()

def generate_image(description: str, num_inference_steps=20) -> Image:
    """
    Gera uma imagem com base em uma descrição textual.

    Args:
        description (str): Descrição da imagem.
        num_inference_steps (int): Passos de inferência.

    Returns:
        Image: Objeto PIL contendo a imagem gerada.
    """
    if not description.strip():
        raise ValueError("A descrição não pode estar vazia.")
    if len(description) > 100:
        description = description[:100]

    result = pipe(description, num_inference_steps=num_inference_steps).images[0]
    return result
