from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
from io import BytesIO
from PIL import Image
import pytesseract
import save
import os
import AI

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
options = Options()
#options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://chromedino.com/")
data = save.get() if os.path.exists("data.json") else ""
network = AI.create_network(240001,[2,8],3) if data == "" else data
new_network = AI.mutate_network(network)
frames = 1

def movements(key=0):
    if key == 1:
        ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
    elif key == 2:
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    elif key == 3:
        ActionChains(driver).send_keys(Keys.SPACE).perform()

def screenshot():
    bytes = driver.get_screenshot_as_png()
    image = Image.open(BytesIO(bytes))
    high_score = pytesseract.image_to_string(image.crop((1010,170,1100,195))).upper().replace("O","0").replace("L","")
    curr_score = pytesseract.image_to_string(image.crop((1110,170,1200,195))).upper().replace("O","0").replace("L","")
    map = image.crop((450,200,850,400))
    return [image,map,int(high_score),int(curr_score)]

sleep(1.5)
movements(3)
sleep(6)
movements(3)

x = 0
while x < frames:
    x += 1
    sleep(0.001)
    img = screenshot()
    listed = list(img[1].getdata())
    extra = [listed[i][z] for i in range(len(listed)) for z in range(3)]
    extra.insert(0,img[3])
    result = AI.calculate(new_network,img)
    movements(result)

sleep(1)
driver.quit()
save.save(new_network)
os.system("cls")
print(f"Current: {img[3]}\nHigh: {img[2]}\n")