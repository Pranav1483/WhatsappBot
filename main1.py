def chat(messages=[], media=None):
    for contact, message in messages:
        time.sleep(10)
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-data-dir={os.getcwd()}/Cookies")
        options.add_argument("--start-maximized")
        s = Service(executable_path=f"{os.getcwd()}/chromedriver.exe")
        browser = webdriver.Chrome(service=s, options=options)
        browser.get("https://www.google.com/")
        actions = ActionChains(browser)
        button = "//div[@id='app']//div[@class='_1Fm4m _1h2dM app-wrapper-web font-fix os-win _13Dep']//div[@class='two _1jJ70']//div[@class='_2Ts6i _2xAQV']//div[@class='_2Ex_b']//footer[@class='_3E8Fg']//div[@class='_2lSWV _3cjY2 copyable-area']//div[@class='_4r9rJ']//span"
        browser.execute_script('window.open();')
        browser.switch_to.window(browser.window_handles[-1])
        browser.get(f"https://web.whatsapp.com/send?phone=91{contact}&text={message}")
        Wait(browser, 100).until(ec.any_of(ec.presence_of_element_located(('class name', '_2UwZ_')), ec.presence_of_element_located(('xpath', f'({button})'))))
        if ec.presence_of_element_located(('class name', '_2UwZ_')):
            Wait(browser, 100).until_not(ec.presence_of_element_located(('class name', '_2UwZ_')))
        Wait(browser, 100).until(ec.presence_of_element_located(('xpath', f'({button})')))
        span = browser.find_elements('xpath', f"{button}")[1]
        textbox = span.find_element('xpath', "//div[@class='_2lryq']//div[@class='_1VZX7']//div[@class='_3Uu1_']//div[@class='g0rxnol2 ln8gz9je lexical-rich-text-input']//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']")
        textbox.send_keys(Keys.CONTROL, 'v')
        Wait(browser, 100).until(ec.presence_of_element_located(('xpath', '(//div[@class="to2l77zo gfz4du6o ag5g9lrv fe5nidar kao4egtt"])')))
        new_textbox = browser.find_element('xpath', '(//div[@class="to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt"])')
        new_textbox.send_keys(Keys.ENTER)
        Wait(browser, 100).until(ec.presence_of_element_located(('xpath', f"({button})")))
        Wait(browser, 1).until(ec.presence_of_element_located(('xpath', '(//span[@data-icon = "msg-time"])')))
        Wait(browser, 100).until_not(ec.presence_of_element_located(('xpath', '(//span[@data-icon = "msg-time"])')))
        browser.quit()
