import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
data = pd.read_csv("File_Name.csv")
data_dict = data.to_dict('list')
leads = data_dict['Number']
messages = data_dict['Message']
combo = zip(leads, messages)
first = True
for lead, message in combo:
    time.sleep(4)
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    time.sleep(6)
    width, height = pg.size()
    pg.click(width/2, height/1.11)
    time.sleep(8)
    pg.press('enter')
    time.sleep(8)
    pg.hotkey('ctrl', 'w')
