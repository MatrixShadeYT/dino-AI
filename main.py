from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
from io import BytesIO
from PIL import Image

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
    high_score = image.crop((1000,170,1100,195))
    curr_score = image.crop((1100,170,1200,195))
    map = image.crop((450,200,1200,400))
    return [image,high_score,curr_score,map]

sleep(2)
movements()
while True:
    sleep(6)
    break
img = screenshot()
driver.quit()