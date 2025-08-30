from io import BytesIO
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def clean_text(text):
    return text.upper().replace("O","0").replace("I","1").replace("L","").replace("S","5").replace("Z","2")

def screenshot(driver):
    bytes = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(bytes))
    high_score = pytesseract.image_to_string(image.crop((1010,170,1100,195)))
    curr_score = pytesseract.image_to_string(image.crop((1110,170,1200,195)))
    map = image.crop((500,200,800,360))
    return [image,map,int(clean_text(high_score)),int(clean_text(curr_score))]