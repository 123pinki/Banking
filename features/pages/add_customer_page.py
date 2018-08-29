from time import sleep


class AddCustomer:
    def __init__(self, driver):
        self.driver = driver

    def select_manager_work(self, work_setting):
        sleep(2)
        work = self.driver.find_elements_by_xpath("/html/body/div/div/div[2]/div/div[1]/button")
        for work_part in work:
            if work_part.text == work_setting:
                work_part.click()

    def first_name(self):
        f_name = self.driver.find_element_by_css_selector("[ng-model='fName']")
        f_name.send_keys("Pinki")

    def last_name(self):
        l_name = self.driver.find_element_by_css_selector("[ng-model='lName']")
        l_name.send_keys("Kumari")

    def postal_code(self):
        postal_code = self.driver.find_element_by_css_selector("[ng-model='postCd']")
        postal_code.send_keys("875578")

    def submit_detail(self):
        self.driver.find_element_by_css_selector("[type='submit']").click()
        alert = self.driver.switch_to.alert
        alert.accept()
