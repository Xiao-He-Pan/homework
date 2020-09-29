# -*- coding: utf-8 -*-
import io
from PIL import Image
import pytesseract

Image=Image.open('1111.png')
text = pytesseract.image_to_string(Image)
print(text)