from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium import webdriver
from time import sleep
import images
import AI

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
options = Options()
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=options)
driver.get("https://chromedino.com/")
Neuron = AI.NeuralNetwork([48001,3])

sleep(2)
movements(1)
sleep(6)
movements(1)

while True:
    sleep(0.001)
    img = images.screenshot(drive)
    listed = list(img[1].getdata())
    extra = [listed[i][0] for i in range(len(listed))]
    extra.insert(0,img[3])
    print([i for i in Neuron.forward(extra,method="softmax")])
    break

sleep(1)
driver.quit()
print(f"Current: {img[3]}\nHigh: {img[2]}\n")