from PIL import Image
image = Image.open('AMOGUS.jpg')
new_image = image.crop((0, 0, 240, 360))
new_image.save("AMO.jpg")
image.close()
new_image.close()

image2 = Image.open('AMOGUS.jpg')
new_image2 = image2.crop((240, 0, 480, 360))
new_image2.save("GUS.jpg")
image2.close()
new_image2.close()