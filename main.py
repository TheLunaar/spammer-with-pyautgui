import pyautogui as auto
import time

while True:
    auto.write("Buraya Spamlamak İstediğiniz Mesajı Yazın")
    auto.press("enter")
    time.sleep(0.5) #Kaç Saniye Aralıklarla Mesaj Göndereceğini Belirtin
