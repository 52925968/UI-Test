from selenium  import  webdriver
from selenium.webdriver.edge.service import  Service
from base_page import BasePage

service=Service('C:/Users/admin/AppData/Local/Google/Chrome/Application/chromedriver.exe')
class WEB_PAGE(BasePage):

    def start(self):

        if self._driver is None:
            options = webdriver.ChromeOptions()
            options.add_argument('--start-maximized')
            options.service = service
            self._driver = webdriver.Chrome(options=options)
            self._driver.implicitly_wait(5)
            print('driver=', self._driver)


    def open(self,url):
        self._driver.get(url)

    def quit(self):
        self._driver.quit()