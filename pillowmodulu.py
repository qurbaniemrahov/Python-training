from PIL import Image,ImageFilter


image = Image.open("test.jpg")
image.save("yeni_test.jpg")

image.rotate(180)

olcu = (900,900)
image.thumbnail(olcu)

#Pillow modulundan esas sekillerle islemek ucun istifade olunur daha etrafli pillow -un documentasiyasina bax



