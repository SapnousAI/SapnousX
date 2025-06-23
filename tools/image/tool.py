try:
    from PIL import Image
    import numpy as np
    image_available = True
except ImportError:
    image_available = False

def resize_image(input_path, output_path, size=(128, 128)):
    if not image_available:
        return 'Pillow not installed.'
    img = Image.open(input_path)
    img = img.resize(size)
    img.save(output_path)
    return f'Image saved to {output_path}'
