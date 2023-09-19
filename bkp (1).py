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
hoje = datetime.today().strftime("%d/%m/%Y")

time.sleep(5)

#clicando em home e diagnostico
pg.click(235, 1026)
time.sleep(2)
pg.click(1679, 1028)
time.sleep(5)


#tirando o primeiro print

for i in range(12):
    snapshot = ImageGrab.grab()
    image = np.array(snapshot)
    cv2.imwrite("imagem" + str(i+1) +".jpg", image)
    if i == 0:
        cv2.imwrite("linha1.jpg", image[180:201, 326:1555]) #y1 y2, x1 x2
        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha1_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[180:201, x + 80:x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            img = cv2.imread(coluna, cv2.IMREAD_UNCHANGED)
            w = int(img.shape[1] * 1)
            h = int(img.shape[0] * 1)
            resized = cv2.resize(img, (w,h), interpolation = cv2.INTER_AREA)
            linha = linha + pytesseract.image_to_string(resized, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",McA," + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha2_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[207:248, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",McA," + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha3_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[265:290, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",McA," + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha4_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[302:333, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",McA," + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha5_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[348:379, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",McA," + linha[:-2] + "\n"


        pg.click(520, 67)
        time.sleep(1)
    elif i <= 10:
        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha1_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[180:201, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",Section"+str(i) + " " + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha2_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[207:248, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",Section"+str(i) + " " + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha3_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[265:290, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",Section"+str(i) + " " + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha4_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[302:333, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",Section"+str(i) + " " + linha[:-2] + "\n"

        pg.click(520, 67)
        time.sleep(1)
    else:
        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha1_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[180:201, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",Whc," + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha2_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[207:248, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            linha = linha + pytesseract.image_to_string(coluna, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",Whc," + linha[:-2] + "\n"

        linha = ""
        x = 326
        for j in range(5):
            coluna = "linha3_" + str(j)+".jpg"
            cv2.imwrite(coluna, image[265:290, x+80 :x + 80 + 100]) #y1 y2, x1 x2
            x = x + 160 + 90
            img = cv2.imread(coluna, cv2.IMREAD_UNCHANGED)
            w = int(img.shape[1] * 1)
            h = int(img.shape[0] * 1)
            resized = cv2.resize(img, (w,h), interpolation = cv2.INTER_AREA)
            linha = linha + pytesseract.image_to_string(resized, config=custom_config).replace("\n", ",")
        dados = dados + hoje + ",Whc," + linha[:-2] + "\n"
        
    #else:
    #    break

print(dados)
#botao proximo (520, 67)
