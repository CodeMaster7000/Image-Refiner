from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont 
  
img = Image.open("input.png") 
draw = ImageDraw.Draw(img) 
  
font = ImageFont.truetype("ComicSansMS3.ttf", 30) 

# Replace with text of your choice
draw.text((50, 100), "ENTER_TEXT_HERE", (255, 255, 255), font=font) 
img.save('sample.jpg') 
