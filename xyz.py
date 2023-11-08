import pytesseract 
from PIL import Image

imgp=r'C:\Users\SivaDsolo\Desktop\pr 2\detection_1674905738.9894335.jpg'

img=Image.open(imgp)

text= pytesseract.image_to_string(img)

print(text)