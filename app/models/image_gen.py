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

# Configuração do modelo para otimização de desempenho
model_id = "CompVis/stable-diffusion-v1-4"

# Usando o agendador EulerDiscreteScheduler (opcional para maior desempenho)
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")

# Carregar o modelo com otimizações, ajustado para CPU
pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    scheduler=scheduler,
    torch_dtype=torch.float32  # Mantém a precisão padrão para CPU
).to("cpu")  # Força o uso da CPU

# Não é necessário dividir a atenção na CPU, mas mantemos para consistência
pipe.enable_attention_slicing()

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

    # Ajuste o número de passos de inferência, caso necessário
    num_inference_steps = 30

    # Gerar a imagem com o prompt fornecido
    result = pipe(description, num_inference_steps=num_inference_steps).images[0]
    return result
