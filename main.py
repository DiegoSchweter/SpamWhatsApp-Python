import pyautogui as spam
import time

limite_msg = input("Qtde mensagens: ")
msg = input("Mensagem: ")

i = 0

time.sleep(2)

while i <= int(limite_msg):
    spam.typewrite(msg)
    spam.press("Enter")
    i += 1

# Agora é só clicar no input do WhatsApp Web e ver acontecer
