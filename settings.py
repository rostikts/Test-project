

desired_cap =[]
desired_cap.append({'browserName': 'chrome', 'version': '', 'platform': 'ANY'})
desired_cap.append({'browserName': 'firefox', 'marionette': True, 'acceptInsecureCerts': True})

def choose_browser():
    print('Browser list:\nGoogle Chrome: 0\nMozilla Firefox: 1')

    try:
        browser_index = int(input("Enter browser's index: "))
        assert browser_index >= 0 and browser_index <= (len(desired_cap)-1), 'Invalid index'
    except:
        print("Invalid index!")
        quit()
    return browser_index