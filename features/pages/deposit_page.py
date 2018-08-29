from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Deposit:
    def __init__(self, driver):
        self.driver = driver

    def select_option(self, setting):
        sleep(3)
        select_item = self.driver.find_elements_by_xpath("/html/body/div/div/div[2]/div/div[3]/button")
        for iten in select_item:
            if iten.text == setting:
                iten.click()

    def enter_deposit_amount(self, amount1):
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[ng-model='amount']")))
        amount = self.driver.find_element_by_css_selector("[ng-model='amount']")
        amount.send_keys(amount1)

    def click_on_deposit(self):
        self.driver.find_element_by_css_selector("[type='submit']").click()
