from Libs.Driver_commands import DriverCommands

class SearchBarPage():
    def __init__(self, driver):
        self.driver = driver
        self.driver_commands = DriverCommands(self.driver)

    #Elements

    def search_button(self):
        self.driver_commands.wait_for_page_to_load()
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/a")

    def search_field(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/input")
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/input")

    def task_bar_button(self):
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select")

    def id_button(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[2]")
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[2]")

    def go_button(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/span/a")
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/span/a")

    def ref_no_button(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[3]")
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[3]")

    def customer_button(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[4]")
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[4]")

    def module_button(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[5]")
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[5]")

    def status_button(self):
        self.driver_commands.wait_for_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[6]")
        return self.driver.find_element_by_xpath(".//*[@id='content']/div[3]/div[2]/div/div/div[1]/div[3]/span[1]/select/option[6]")

    #Actions

    def click_search_button(self):
        self.search_button().click()

    def click_id_button(self):
        self.id_button().click()

    def click_task_bar_button(self):
        self.task_bar_button().click()

    def click_go_button(self):
        self.go_button().click()

    def click_ref_no_button(self):
        self.ref_no_button().click()

    def click_customer_button(self):
        self.customer_button().click()

    def click_module_button(self):
        self.module_button().click()

    def click_status_button(self):
        self.status_button().click()

    def fill_search_field(self, text):
        self.search_field().send_keys(text)

    #Function

    def id_search(self, id):
        self.click_search_button()
        self.fill_search_field(id)
        self.click_task_bar_button()
        self.click_id_button()
        self.click_go_button()

    def ref_no_search(self, no):
        self.click_search_button()
        self.fill_search_field(no)
        self.click_task_bar_button()
        self.click_ref_no_button()
        self.click_go_button()

    def customer_search(self, name):
        self.click_search_button()
        self.fill_search_field(name)
        self.click_task_bar_button()
        self.click_customer_button()
        self.click_go_button()

    def module_search(self, module):
        self.click_search_button()
        self.fill_search_field(module)
        self.click_task_bar_button()
        self.click_module_button()
        self.click_go_button()

    def status_search(self, status):
        self.click_search_button()
        self.fill_search_field(status)
        self.click_task_bar_button()
        self.click_status_button()
        self.click_go_button()