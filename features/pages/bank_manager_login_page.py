

class BankManager:
    def __init__(self, driver):
        self.driver = driver

    def click_on_bank_manager_login(self):
        self.driver.find_element_by_css_selector("[ng-click='manager()']").click()
