from Libs.Driver_commands import DriverCommands

class TopBar():
    def __init__(self, driver):
        self.driver = driver
        self.driver_commands = DriverCommands(self.driver)

    #Elements

    def home_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[1]/a")

    def hotel_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[2]/a")

    def flight_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[3]/a")

    def tours_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[4]/a")

    def cars_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[5]/a")

    def offers_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[6]/a")

    def blog_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[7]/a")

    def contact_us_button(self):
        return self.driver.find_element_by_xpath("html/body/nav[1]/div/div/div/ul/li[8]/a")

    #Actions

    def click_home_button(self):
        self.home_button().click()
        self.driver_commands.wait_for_page_to_load()

    def click_hotel_button(self):
        self.hotel_button().click()
        self.driver_commands.wait_for_page_to_load()

    def click_flight_button(self):
        self.flight_button().click()
        self.driver_commands.wait_for_page_to_load()

    def click_tours_button(self):
        self.tours_button().click()
        self.driver_commands.wait_for_page_to_load()

    def click_cars_button(self):
        self.cars_button().click()
        self.driver_commands.wait_for_page_to_load()

    def click_offers_button(self):
        self.offers_button().click()
        self.driver_commands.wait_for_page_to_load()

    def click_blog_button(self):
        self.blog_button().click()
        self.driver_commands.wait_for_page_to_load()

    def click_contact_us_button(self):
        self.contact_us_button().click()
        self.driver_commands.wait_for_page_to_load()

