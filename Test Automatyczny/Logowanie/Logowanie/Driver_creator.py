from selenium import webdriver

def create_driver():
    geckodriver = "C:\Program Files (x86)\Gecko Driver\geckodriver.exe"    #praca w tle
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    driver = webdriver.Firefox(executable_path=geckodriver, firefox_options=options)
    #driver = webdriver.Firefox()  # wywołanie strony podczas testu
    return driver
