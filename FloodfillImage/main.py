from PIL import Image, ImageDraw

img = Image.open(R"input.png")
img1 = img.convert("RGB") 
 
seed = (1, 2) # Replace values with those of the image 
rep_value = (255, 255, 0) # Replace values
ImageDraw.floodfill(img, seed, rep_value, thresh=50)
  
img.show()
