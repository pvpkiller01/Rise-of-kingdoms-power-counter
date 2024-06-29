import pytesseract as tess
import pyautogui
tess.pytesseract.tesseract_cmd = r'C:\Users\Utilizador\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
import tkinter as tk
import time
import re
# img = Image.open('image3.png')
# text = tess.image_to_string(img)



global soma
soma = 0
quantidadeSomada = 0
#pyautogui.displayMousePosition()
def capturar_e_extrair_texto():
    i = 0
    while i <50:
        global soma
        global quantidadeSomada
        x = 1355
        y = 312
        largura = 200
        altura = 638
        
        imagem = pyautogui.screenshot(region=(x, y, largura, altura))
        imagem.save("captura_porcao.png")
        texto_extraido = tess.image_to_string(imagem)
        numeros_apenas = re.sub(r'[^0-9\s]', '', texto_extraido)
        numeros_lista = numeros_apenas.split()
        
        for numero in numeros_lista:
            #soma += int(numero)
            numero_bom = re.sub(r'[^\d]', '', numero)
            if(int(numero_bom)!=7):
                soma+=int(numero_bom)
                print(numero_bom)
                quantidadeSomada+=1
            
        total = 'The total power is:' + str(soma)
        media='The average power is:' + str(soma/((i+1)*6))
        quantidadeSoma = 'The quantity of accounts summed: ' + str(quantidadeSomada)
        texto_label.config(text=texto_extraido + "\n" + total + "\n" + media + "\n" + quantidadeSoma, font=("Arial", 25))

        time.sleep(0.01)
        clique(931,968)
        i+=1
        print('---------------------------------------------------------')

def clique(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    pyautogui.moveRel(0, -712, duration=1)
    time.sleep(0.5)
    pyautogui.mouseUp()


root = tk.Tk()
root.title("Captura de tela")

# Cria um botão para capturar a tela
botao = tk.Button(root, text="Capturar e extrair texto", command=capturar_e_extrair_texto)
botao.pack(pady=10)


# Cria um rótulo para exibir o texto extraído
texto_label = tk.Label(root, text="")
texto_label.pack(pady=10)

root.mainloop()

#text = text[:-1]
#text = text.replace('.','')
