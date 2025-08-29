from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://chromedino.com/")
driver.save_screenshot("screenshot.png")
screenshot_bytes = driver.get_screenshot_as_png()

print(f"\nScreenshot captured ({len(screenshot_bytes)} bytes)")
print("Program Over!")
driver.quit()