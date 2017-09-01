import unittest

import time

from Libs import Driver_creator
from Libs.Driver_commands import DriverCommands
from Page.Login_page import LoginPage
from Page.Main_page import MainPage
from Page.Account_page import AccountPage
from Page.Top_bar import TopBar
from Page.Search_bar_page import SearchBarPage
from Page.Admin_page import AdminPage


class WebTest1(unittest.TestCase):

    def setUp(self):
        self.driver = Driver_creator.create_driver()
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.driver_commands = DriverCommands(self.driver)
        self.account_page = AccountPage(self.driver)
        self.top_bar = TopBar(self.driver)
        self.search_bar_page = SearchBarPage(self.driver)
        self.admin_page = AdminPage(self.driver)

    def test_01_correct_login_and_password(self):
        self.driver_commands.open_page("http://www.phptravels.net/")
        self.main_page.click_main_button()
        self.main_page.click_login_button()
        self.login_page.login("user@phptravels.com", "demouser")
        assert self.account_page.check_login_result() is True

    def test_02_correct_login_invalid_password(self):
        self.driver_commands.open_page("http://www.phptravels.net/")
        self.main_page.click_main_button()
        self.main_page.click_login_button()
        self.login_page.login("user@phptravels.com", "duser")
        assert self.account_page.check_invalid_login_result() is True

    def test_03_invalid_login_correct_password(self):
        self.driver_commands.open_page("http://www.phptravels.net/")
        self.main_page.click_main_button()
        self.main_page.click_login_button()
        self.login_page.login("user@travels.com", "demouser")
        assert self.account_page.check_invalid_login_result() is True

    def test_04_no_login_correct_password(self):
        self.driver_commands.open_page("http://www.phptravels.net/")
        self.main_page.click_main_button()
        self.main_page.click_login_button()
        self.login_page.login("", "demouser")
        assert self.account_page.check_invalid_login_result() is True

    def test_05_correct_login_no_password(self):
        self.driver_commands.open_page("http://www.phptravels.net/")
        self.main_page.click_main_button()
        self.main_page.click_login_button()
        self.login_page.login("user@phptravels.com", "")
        assert self.account_page.check_invalid_login_result() is True

    def test_06_top_button_test(self):
        self.driver_commands.open_page("http://www.phptravels.net/")
        self.top_bar.click_hotel_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/properties/"
        self.top_bar.click_flight_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/flight"
        self.top_bar.click_tours_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/tours"
        self.top_bar.click_cars_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/car"
        self.top_bar.click_offers_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/offers"
        self.top_bar.click_blog_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/blog"
        self.top_bar.click_contact_us_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/contact-us"
        self.top_bar.click_home_button()
        assert self.driver_commands.return_url() == "http://www.phptravels.net/"

    def test_07_id_search_test(self):
        self.driver_commands.open_page("http://www.phptravels.net/admin")
        self.login_page.admin_login("admin@phptravels.com", "demoadmin")
        self.search_bar_page.id_search("47")
        #assert self.admin_page.check_id_result() is True

    def test_08_ref_no_search_test(self):
        self.driver_commands.open_page("http://www.phptravels.net/admin")
        self.login_page.admin_login("admin@phptravels.com", "demoadmin")
        self.search_bar_page.ref_no_search("7504")
        #assert self.admin_page.check_ref_no_result() is True

    def test_09_customer_search_test(self):
        self.driver_commands.open_page("http://www.phptravels.net/admin")
        self.login_page.admin_login("admin@phptravels.com", "demoadmin")
        self.search_bar_page.customer_search("John")
        #assert self.admin_page.check_customer_result() is True

    def test_10_module_search_test(self):
        self.driver_commands.open_page("http://www.phptravels.net/admin")
        self.login_page.admin_login("admin@phptravels.com", "demoadmin")
        self.search_bar_page.module_search("hotels")

    def test_11_status_search_test(self):
        self.driver_commands.open_page("http://www.phptravels.net/admin")
        self.login_page.admin_login("admin@phptravels.com", "demoadmin")
        self.search_bar_page.status_search("unpaid")

    def tearDown(self):
        self.driver.save_screenshot('screenie.png')
        self.driver.close()
