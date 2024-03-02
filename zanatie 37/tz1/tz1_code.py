from PIL import Image
image = Image.open('Amogus1.jpg')
image=image.rotate(90)
image.show()
a=input("Как повернуть картинку? ")
if a == "px":
    new_image = image.rotate(90)
    new_image.save("new_Amogus1.jpg")
    image.close()
    new_image.close()
    
image = Image.open('Amogus2.jpg')
image=image.rotate(180)
image.show()
a=input("Как повернуть картинку? ")
if a == "vn":
    new_image = image.rotate(180)
    new_image.save("new_Amogus2.jpg")
    image.close()
    new_image.close()   


