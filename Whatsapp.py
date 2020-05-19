import webbrowser                  # for opening whatsapp web using the default browser
import pyautogui as pg             # for automate the movement and clicks of keyboard and mouse.
import time

webbrowser.open('https://web.whatsapp.com/send?phone= -,&text=Hey!')
# phone = "number with country code to which you want to send the message" -> eg: +91 xxx-xxx-xxxx 
# text = "text that you want to send" -> eg: send = HEY!! (this will show "HEY" on the sender's message box but will not send it)

time.sleep(10)                      # In case whatsapp'll take time to open due to internet connectivity.

pg.press('enter')                   # This will automatically press "enter" on the keyboard & message will be send.
