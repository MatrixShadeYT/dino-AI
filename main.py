from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("chrome://dino")

def screenshot(name="dino.png"):
    driver.save_screenshot(name)
    return name

driver.quit()