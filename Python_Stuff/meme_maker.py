from PIL import Image, ImageDraw, ImageFont
import sys

# Get commit message from GitHub Action
commit_msg = sys.argv[1] if len(sys.argv) > 1 else "Default Meme Text"

# Load a meme template (you’ll need to add one)
img = Image.open("meme-template.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()

# Overlay text
draw.text((10, 10), commit_msg, font=font, fill="white")
img.save("meme-output.png")