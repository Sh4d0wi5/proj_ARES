from PIL import Image

#path = r"D:\Codex\Proj_ARES\Asset\road.jpg"
image = cv2.imread("Asset/road.jpg")

try:
    img = Image.open(path)
    print("Actual format:", img.format)
    print("Image size:", img.size)
    print("Image mode:", img.mode)
    img.verify()
    print("Image verification: Successful")

except Exception as e:
    print("Image error:", e)

###################### IMage COnversion ######################

input_path = r"D:\Codex\Proj_ARES\Asset\heli.jpg"
output_path = r"D:\Codex\Proj_ARES\Asset\heli_converted.jpg"

img = Image.open(input_path)
img.convert("RGB").save(output_path, "JPEG", quality=95)

print("Conversion successful!")