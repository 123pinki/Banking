# from selenium import webdriver


class CustomerLogin:
    def __init__(self, driver):
        self.driver = driver

    def click_on_banking(self):
        # self.driver = webdriver.Firefox()
        self.driver.get("http://www.globalsqa.com/angularjs-protractor-practice-site")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 500)")
        self.driver.find_element_by_link_text("Banking").click()

    def customer_login(self):
        self.driver.find_element_by_css_selector("[ng-click='customer()']").click()

    def select_name(self):
        self.driver.find_element_by_name("userSelect").click()
        self.driver.find_element_by_xpath("//*[@id='userSelect']/option[2]").click()

    def login(self):
        self.driver.find_element_by_css_selector("[type='submit']").click()

    def select_account_number(self):
        self.driver.find_element_by_name("accountSelect").click()
        self.driver.find_element_by_xpath("//*[@id='accountSelect']/option[1]").click()

    def logout(self):
        self.driver.find_element_by_css_selector("[ng-click='byebye()']").click()

    def home(self):
        self.driver.find_element_by_css_selector("[ng-click='home()']").click()
