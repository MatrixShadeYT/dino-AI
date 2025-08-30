from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
from io import BytesIO
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
options = Options()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://chromedino.com/")

def movements(key=0):
    if key == 1:
        ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
    elif key == 2:
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    else:
        ActionChains(driver).send_keys(Keys.SPACE).perform()
    return
def screenshot():
    bytes = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(bytes))
    high_score = pytesseract.image_to_string(image.crop((1010,170,1100,195))).upper().replace("O","0").replace("L","")
    curr_score = pytesseract.image_to_string(image.crop((1110,170,1200,195))).upper().replace("O","0").replace("L","")
    map = image.crop((450,200,850,400))
    return [image,map,int(high_score),int(curr_score)]

sleep(1.5)
movements()
sleep(6)
movements()

while True:
    sleep(0.01)
    img = screenshot()
    listed = [img[2],img[3]]
    pixels = list(img[1].convert("RGB").getdata())
    for i in range(pixels):
        for x in range(pixels[i+1]):
            listed.append(pixels[i+1])
    AI(img)
    break

sleep(1)
img = screenshot()
driver.quit()
print(f"\nCurrent: {img[3]}\nHigh: {img[2]}\n")