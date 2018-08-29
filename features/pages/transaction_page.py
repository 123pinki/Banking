

class Transaction:
    def __init__(self, driver):
        self.driver = driver

    def reset(self):
        self.driver.find_element_by_css_selector("[ng-click='reset()']").click()

    def back(self):
        self.driver.find_element_by_css_selector("[ng-click='back()']").click()