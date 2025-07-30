from PIL import Image, ImageDraw, ImageFont
import sys
import os

# Get commit message 
commit_msg = sys.argv[1] if len(sys.argv) > 1 else "Default Meme Text"

# Use correct path to template (go up one directory from Python_Stuff)
template_path = os.path.join(os.path.dirname(__file__), '../Python_Stuff/images/meme-template.jpg')

try:
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()   
    
    # Add text (adjust position as needed)
    draw.text((50, 50), commit_msg, font=font, fill="black")
    
    # Save output
    output_path = os.path.join(os.path.dirname(__file__), 'meme-output.png')
    img.save(output_path)
    print(f"Meme saved to {output_path}")
except FileNotFoundError:
    print(f"Error: Could not find template at {template_path}")
    sys.exit(1)