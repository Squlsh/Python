import os

from time import strftime

class DriverHelpers():

    def __init__(self, driver):
        self.driver = driver

    def save_screenshot(self, testName):
        testName = testName.split('.')[2]
        self.driver.save_screenshot("test_results\{}_problem_{}.png".format(curTime, testName))

    def ip_adress(self):
        filetxt = "ip.txt"
        ipadd = []
        if os.path.isfile(filetxt):
            with open(filetxt, 'r') as content:
                for line in content:
                    line = line.replace("\r", "").replace("\n", "")
                    ipadd.append(line)
        return ipadd

curTime = strftime("%Y_%m_%d_%H_%M_%S")
