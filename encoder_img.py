import base64

image_path = "images/tower.jpeg"
image_path2 = "images/mountain.jpeg"
image_path3 = "images/skellySword.jpeg"
image_path4 = "images/shop.jpeg"

with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

with open(image_path2, "rb") as image_file:
    encoded_image2 = base64.b64encode(image_file.read()).decode('utf-8')

with open(image_path3, "rb") as image_file:
    encoded_image3 = base64.b64encode(image_file.read()).decode('utf-8')

with open(image_path4, "rb") as image_file:
    encoded_image4 = base64.b64encode(image_file.read()).decode('utf-8')

with open("encoded_images.txt","w")as f:
    f.write("Tower:\n"+encoded_image + "\n\n")
    f.write("Mountain:\n"+encoded_image2 + "\n\n")
    f.write("Skelly:\n"+encoded_image3 + "\n\n")
    f.write("Shop:\n"+encoded_image4 + "\n\n")
# print(encoded_image[:100])
# print("\n")
# print(encoded_image2)
# print("\n")
# print(encoded_image3)
# print("\n")
# print(encoded_image4)
