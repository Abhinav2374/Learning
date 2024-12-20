import pytesseract
import cv2

image = cv2.imread()

greyimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string()
