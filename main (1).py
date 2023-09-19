import pyautogui as pg 
import time
from PIL import ImageGrab
import cv2
import numpy as np
import pytesseract
from datetime import datetime

dados = ""
custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=.0123456789'
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
hoje = datetime.today().strftime("%d/%m/%Y %H:%M")

time.sleep(5)
#clicando em home e diagnostico
pg.click(235, 1026)
time.sleep(3)
pg.click(1679, 1028)

time.sleep(5)

def get_linha(y1, y2, nome, indice):
    global dados
    coluna = "linha" + str(indice) + ".png"
    cv2.imwrite(coluna, image[y1:y2, 326:1555]) #y1 y2, x1 x2
    img = cv2.imread(coluna, cv2.IMREAD_UNCHANGED)
    w = int(img.shape[1] * 2.5)
    h = int(img.shape[0] * 2.5)
    resized = cv2.resize(img, (w,h), interpolation = cv2.INTER_AREA)
    linha = pytesseract.image_to_string(resized, config=custom_config).replace(" ", ",")
    dados = dados + hoje + "," + nome + "," + linha
    


#tirando o primeiro print

for i in range(11):
    snapshot = ImageGrab.grab()
    image = np.array(snapshot)
    cv2.imwrite("imagem" + str(i+1) +".png", image)
    if i == 0:
        get_linha(180,201, "Tube Rotation", 1)
        get_linha(207,248, "Tube Height", 2)
        get_linha(265,290, "Feeder Plunger", 3)
        get_linha(302,333, "Shear", 4)
        get_linha(348,379, "Gob", 5)


        pg.click(520, 67)
        time.sleep(4)
    elif i:
        get_linha(180,201, "Invert" + str(i), 1)
        get_linha(207,248, "TakeOut" + str(i), 2)
        get_linha(265,290, "PusherArm" + str(i), 3)
        get_linha(302,333, "Pusher Finger" + str(i), 4)

        pg.click(520, 67)
        time.sleep(4)
    # else:
      #   get_linha(180,201, "Machine Conveyor", 1)
      #   get_linha(207,248, "Ware Transfer", 2)
      #   get_linha(265,290, "Cross Conveyor", 3)
     #    time.sleep(4)
    #    break
pg.click(235, 1026)

with open("variaveis_do_servo.txt", "w") as myfile:
    myfile.write(dados)
print(dados)
with open("variaveis_do_servo2.txt", "a") as myfile:
    myfile.write(dados)
print(dados)
#botao proximo (520, 67)


