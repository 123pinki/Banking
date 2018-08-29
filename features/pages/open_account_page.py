

class OpenAccount:
    def __init__(self, driver):
        self.driver = driver

    def currency(self):
        self.driver.find_element_by_name("currency").click()
        self.driver.find_element_by_xpath("//*[@id='currency']/option[2]").click()

    def process(self):
        self.driver.find_element_by_css_selector("[type='submit']").click()
        alert = self.driver.switch_to.alert
        alert.accept()
