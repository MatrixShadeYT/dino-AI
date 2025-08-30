from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
import numpy as np
import images
import AI

options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://chromedino.com/")
Neuron = AI.NeuralNetwork([48001,3])

def movements(key=0):
    if key == 1:
        ActionChains(driver).send_keys(Keys.ARROW_UP).perform()
    elif key == 2:
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()

sleep(2)
movements(1)
sleep(6)
movements(1)

for i in range(1):
    sleep(0.001)
    img = images.screenshot(driver)
    extra = [list(img[1].getdata())[i][0] for i in range(len(list(img[1].getdata())))]
    print(np.argmax(Neuron.forward(extra,method='softmax'),axis=0))
    break

sleep(1)
driver.quit()
print(f"Current: {img[3]}\nHigh: {img[2]}\n")