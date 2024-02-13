povernut=input("как повернуть амогуса?-")
from PIL import Image
 
image = Image.open('img.jpg')
new_image = image.rotate(180)
new_image.save("rotated_img.jpg")
image.close()
new_image.close()













