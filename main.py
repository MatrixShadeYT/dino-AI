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
sleep(1)
movements()
sleep(1)
bytes = driver.get_screenshot_as_png()
image = Image.open(BytesIO(bytes))
for x in range(100):
    for y in range(25):
        image.putpixel([1100+x,170+y],value=(0,255,0))
for x in range(750):
    for y in range(200):
        image.putpixel([450+x,200+y],value=(0,0,255))
image.show()
driver.quit()