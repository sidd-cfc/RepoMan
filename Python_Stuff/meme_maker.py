import os
from PIL import Image, ImageDraw 

def create_meme(input_path, output_path): 
    try:
        # Verify file exists
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        img = Image.open(input_path)
        draw = ImageDraw.Draw(img)
        
        # Add sample text (customize this!)
        draw.text((50, 20), "GitHub Actions Meme", fill="black")
        
        # Create output directory if needed
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        img.save(output_path)
        print(f"Meme saved to {output_path}")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    
    if not create_meme(args.input, args.output):
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