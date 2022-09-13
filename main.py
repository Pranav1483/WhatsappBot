from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait as Wait
import selenium.webdriver.support.expected_conditions as ec
import os


def chat(lead, message):
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir='+os.getcwd())
    browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    browser.get('https://web.whatsapp.com/send?phone='+str(lead)+'&text='+message)
    Wait(browser, 50).until(ec.any_of(ec.presence_of_element_located(('class name', '_2UwZ_')), ec.presence_of_element_located(('xpath', '(.//div[@class = "fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv"])'))))
    if ec.presence_of_element_located(('class name', '_2UwZ_')):
        Wait(browser, 20).until_not(ec.presence_of_element_located(('class name', '_2UwZ_')))
    Wait(browser, 20).until(ec.presence_of_element_located(('xpath', '(.//div[@class = "fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv"])')))
    browser.find_element('xpath', '(.//div[@class = "fd365im1 to2l77zo bbv8nyr4 mwp4sxku gfz4du6o ag5g9lrv"])').send_keys(Keys.ENTER)
    Wait(browser, 20).until_not(ec.presence_of_element_located(('xpath', '(.//span[@data-testid = "msg-time"])')))
    browser.quit()


df = pd.read_csv('contact.csv')
content = df.to_dict('list')
combo = zip(content['Number'], content['Message'])
for l, m in combo:
    chat(l, m)
