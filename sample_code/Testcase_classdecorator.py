import unittest

from selenium import webdriver


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.title

        cls.driver.get("http://www.google.co.in")

    def test_search_by_category(self):
        self.search = self.driver.find_element_by_name("q")
        self.search.clear()

        self.search.send_keys("phones")
        self.search.submit()
        self.driver.implicitly_wait(30)
        products = self.driver.find_elements_by_xpath("//h3[@class='r']/a")

        self.assertEqual(10, len(products))

    def test_search_by_product(self):
        self.search = self.driver.find_element_by_name("q")
        self.search.clear()

        self.search.send_keys("computer")
        self.search.submit()
        self.driver.implicitly_wait(30)
        products = self.driver.find_elements_by_xpath("//h3[@class='r']/a")

        self.assertEqual(10, len(products));


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main()


