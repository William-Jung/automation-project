from selenium import webdriver


class Controller(object):

    driver = None

    def __init__(self, driver):
        self.driver = driver

    def open_chrome(self):
        self.driver = webdriver.Chrome(executable_path='/Users/ilionailiadhi/Ora/automation-project/chromedriver')

    def input_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def quit_driver(self):
        self.driver.quit()
