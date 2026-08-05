import base64
from io import BytesIO

from PIL import Image


def image_to_bytes(image: Image.Image) -> str:
    buffer = BytesIO()

    if image.mode != "RGB":
        image = image.convert("RGB")

    image.save(buffer, format="PNG")

    image_base64 = base64.b64encode(buffer.getvalue()).decode()

    return image_base64
