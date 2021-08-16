import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class TestCaseTemp(unittest.TestCase):
    """Sample test cases in python"""

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_case_1(self):
        try:
            self.driver.get('https://the-internet.herokuapp.com/')
            el = self.driver.find_element_by_css_selector("a[href='/dropdown']")
            el.click()

        except NoSuchElementException as ex:
            self.fail(ex.msg)

    def test_case_2(self):
        try:
            el1 = self.driver.find_element_by_css_selector('#dropdown')
            el1.click()
        except NoSuchElementException as ex2:
            self.fail(ex2.msg)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseTemp)
    unittest.TextTestRunner(verbosity=2).run(suite)