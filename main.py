from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
from io import BytesIO
from PIL import Image

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://chromedino.com/")
sleep(1)
bytes = driver.get_screenshot_as_png()
print(f"\nScreenshot captured ({len(bytes)} bytes)")
image = Image.open(BytesIO(bytes))
pixels = list(image.getdata())
print(f"Image Size: {image.size}")
print(f"Pixels: {pixels[:1]}")
sleep(1)
driver.quit()