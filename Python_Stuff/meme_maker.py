import argparse
from PIL import Image, ImageDraw, ImageFont

# Set up command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Path to template image')
parser.add_argument('--output', required=True, help='Path to save meme')
args = parser.parse_args()

# Load template
try:
    img = Image.open(args.input)
    draw = ImageDraw.Draw(img)
    
    # Add sample text (customize this!)
    draw.text((10, 10), "Hello from GitHub Actions!", fill="black")
    
    # Save output
    img.save(args.output)
    print(f"Success! Meme saved to {args.output}")
except Exception as e:
    print(f"Error: {str(e)}")
    exit(1)



# from PIL import Image, ImageDraw, ImageFont
# import sys
# import os

# # Get commit message 
# commit_msg = sys.argv[1] if len(sys.argv) > 1 else "Default Meme Text"

# # Use correct path to template (go up one directory from Python_Stuff)
# template_path = os.path.join(os.path.dirname(__file__), '../Python_Stuff/images/meme-template.jpg')

# try:
#     img = Image.open(template_path)
#     draw = ImageDraw.Draw(img)
#     font = ImageFont.load_default()   
    
#     # Add text (adjust position as needed)
#     draw.text((50, 50), commit_msg, font=font, fill="black")
    
#     # Save output
#     output_path = os.path.join(os.path.dirname(__file__), 'meme-output.png')
#     img.save(output_path)
#     print(f"Meme saved to {output_path}")
# except FileNotFoundError:
#     print(f"Error: Could not find template at {template_path}")
#     sys.exit(1)