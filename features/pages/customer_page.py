

class Customer:
    def __init__(self, driver):
        self.driver = driver

    def search_customer_name(self):
        search = self.driver.find_element_by_css_selector("[ng-model='searchCustomer']")
        search.send_keys("Neville")

    def delete_customer(self):
        self.driver.find_element_by_css_selector("[ng-click='deleteCust(cust)']").click()