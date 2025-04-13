from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_image(text, output_path):
    # Create a new image with a gradient background
    width, height = 800, 600
    image = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Create gradient background
    for y in range(height):
        for x in range(width):
            r = int(0 + (x / width) * 0)
            g = int(0 + (y / height) * 255)
            b = int(0 + (x / width) * 0)
            draw.point((x, y), fill=(r, g, b))
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()
    
    # Get text bbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((width - text_width) // 2, (height - text_height) // 2)
    draw.text(position, text, font=font, fill=(255, 255, 255))
    
    # Save the image
    image.save(output_path)

def create_profile_image(output_path):
    # Create a circular profile image
    size = 400
    image = Image.new('RGB', (size, size), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Create gradient background
    for y in range(size):
        for x in range(size):
            r = int(0 + (x / size) * 0)
            g = int(0 + (y / size) * 255)
            b = int(0 + (x / size) * 0)
            draw.point((x, y), fill=(r, g, b))
    
    # Add text
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()
    
    text = "Profile Photo"
    # Get text bbox
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = ((size - text_width) // 2, (size - text_height) // 2)
    draw.text(position, text, font=font, fill=(255, 255, 255))
    
    # Create circular mask
    mask = Image.new('L', (size, size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size, size), fill=255)
    
    # Apply mask
    image.putalpha(mask)
    
    # Save the image as PNG
    output_path = output_path.replace('.jpg', '.png')
    image.save(output_path)

def main():
    # Create projects directory if it doesn't exist
    os.makedirs('app/static/images/projects', exist_ok=True)
    
    # List of projects
    projects = [
        'stat_arb',
        'portfolio_opt',
        'market_micro',
        'ml_trading',
        'risk_management',
        'data_analysis',
        'nlp_finance',
        'blockchain',
        'quant_research',
        'trading_bot'
    ]
    
    # Generate project images
    for project in projects:
        output_path = f'app/static/images/projects/{project}.jpg'
        create_placeholder_image(project.replace('_', ' ').title(), output_path)
    
    # Generate profile image
    create_profile_image('app/static/images/profile.jpg')

if __name__ == '__main__':
    main() 