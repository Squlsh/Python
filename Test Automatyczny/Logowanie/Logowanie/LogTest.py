import unittest
import xmlrunner

from time import strftime
from Libs import Driver_creator
from Libs.Driver_commands import DriverCommands
from Libs.Driver_helpers import DriverHelpers
from Page.Login_page import LoginPage
from Page.Account_page import AccountPage

class EnergyLogSerwerTest(unittest.TestCase):

    driver = None
    passed = False

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver_creator.create_driver()
        cls.driver_commands = DriverCommands(cls.driver)
        cls.driver_helpers = DriverHelpers(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.account_page = AccountPage(cls.driver)

    def setUp(self):
        self.testName = self.id()
        self.passed = False

    def test_01_correct_login_and_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("testowy", "bla123")
            assert self.account_page.check_login_result(self.testName)
            self.driver.get("https://10.4.11.244:5601/logout")
            self.passed = True

    def test_02_correct_login_invalid_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("testowy", "admin123")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_03_invalid_login_correct_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("user89", "bla123")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_04_no_login_correct_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login(" ", "bla123")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_05_correct_login_no_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("testowy", " ")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_06_admin_correct_login_and_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("logserver", "logserver")
            assert self.account_page.check_admin_login_result(self.testName)
            self.driver.get("https://10.4.11.244:5601/logout")
            self.passed = True

    def test_07_admin_correct_login_invalid_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("logserver", "user213")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_08_admin_invalid_login_correct_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("admin44", "logserver")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_09_no_admin_login_correct_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login(" ", "logserver")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_10_admin_correct_login_no_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("logserver", " ")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_11_admin_login_user_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("logserver", "bla123")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def test_12_user_login_admin_password(self):
        ips = self.driver_helpers.ip_adress()
        for ip in ips:
            self.driver_commands.open_page(ip)
            self.login_page.login("testowy", "logserver")
            assert self.account_page.check_invalid_login_result(self.testName)
            self.passed = True

    def tearDown(self):
        if self.passed == False:
            self.driver_helpers.save_screenshot(self.testName)
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    curTime = strftime("%Y_%m_%d_%H_%M_%S")
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test_results', outsuffix=curTime, verbosity=2),
    failfast=False, buffer=False, catchbreak=False)

