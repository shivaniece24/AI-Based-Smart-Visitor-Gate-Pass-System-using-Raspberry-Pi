from PIL import Image, ImageDraw

def create_gate_pass(name):

    image = Image.new('RGB', (500,300), color='white')

    draw = ImageDraw.Draw(image)

    draw.text((50,50), "SMART VISITOR GATE PASS", fill='black')

    draw.text((50,120), f"Visitor: {name}", fill='black')

    filename = f"gatepasses/{name}.png"

    image.save(filename)

    return filename
