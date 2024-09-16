import pyautogui
# import time

# time.sleep(3)
# print(pyautogui.position())

pyautogui.PAUSE = 1

pyautogui.press("win") #pressiona a tecla Window
pyautogui.write("notepad") #Escre a palavra desejada
pyautogui.press("enter")

pyautogui.click(x=666, y=424)
pyautogui.write("Eu tEu te Amoe Amo")

#Descobrir a posição -> pyautogui.position()
#Caso eu queira apagar -> pyautogui.press("backspace")