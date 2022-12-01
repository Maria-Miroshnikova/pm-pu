import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

URL_page_search = 'index.php'
URL_page_filter = 'https://www.kinopoisk.ru/s/'
URL_captcha = 'showcaptcha'

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Edge()

    def test_name_empty(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#find_people")
        element.clear()
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_8.submit.nice_button')
        # check button disable
        if btn.is_enabled():
            print("FAIL: test_name_empty")
        else:
            print("SUCCESS: test_name_empty")

    def test_name_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_correct = ["ларс фон", "фон-триер"]
        for text in text_correct:
            element = driver.find_element(By.CSS_SELECTOR, "input#find_people")
            self.submitInput(element, text)
            # expect no exception
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_name_correct, text=", text)
            # go back
            self.goBack()

    def test_name_wrong(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_wrong = ["#$!%", "брэд, нортон", "брэд;;;;", "1234"]
        for text in text_wrong:
            element = driver.find_element(By.CSS_SELECTOR, "input#find_people")
            self.submitInput(element, text)
            # expect exception
            if (URL_page_filter not in driver.current_url):
                print("FAIL: test_name_wrong, text=", text)
            # go back
            self.goBack()

    def test_year_empty(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#birthday")
        element.clear()
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_8.submit.nice_button')
        # check button disable
        if btn.is_enabled():
            print("FAIL: test_year_empty")
        else:
            print("SUCCESS: test_year_empty")

    def test_year_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_correct = ["1999"]
        for text in text_correct:
            element = driver.find_element(By.CSS_SELECTOR, "input#birthday")
            self.submitInput(element, text)
            # expect no exception
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_year_correct, text=", text)
            # go back
            self.goBack()

    def test_year_wrong(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_wrong = ["1200", "99", "999", "19 99", "19999", "aaa", "1999$"]
        for text in text_wrong:
            element = driver.find_element(By.CSS_SELECTOR, "input#birthday")
            self.submitInput(element, text)
            driver.implicitly_wait(2)
            #push = driver.find_element(By.CLASS_NAME, 'ui_notice ui_widget')

            # expect exception
            if (URL_page_filter not in driver.current_url):
                print("FAIL: test_year_wrong, text=", text)
            # go back
            self.goBack()

    def test_film_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_correct = ["a", "или как", "когда?", "@%&*!"]
        # установка главного поля
        for text in text_correct:
            element = driver.find_element(By.NAME, "m_act[film]")
            self.submitInput(element, text)
            # expect no exception
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_film_correct, text=", text)
            # go back
            self.goBack()

    def test_address_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_correct = ["a", "Верхняя Пышма", "Ростов-на-Дону"]
        # установка главного поля
        for text in text_correct:
            element = driver.find_element(By.NAME, "m_act[location]")
            self.submitInput(element, text)
            # expect no exception, go to result page
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_address_correct, text=", text)
            # go back
            self.goBack()

    def test_address_wrong(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_wrong = ["Пышма#$", "112"]
        # установка главного поля
        for text in text_wrong:
            element = driver.find_element(By.NAME, "m_act[location]")
            self.submitInput(element, text)
            # expect exception
            if (URL_page_filter not in driver.current_url):
                print("FAIL: test_address_wrong, text=", text)
            # go back
            self.goBack()

    ###### INTEGRATION

    def test_name_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#find_people")
        element.clear()
        element.send_keys("иван")
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_8.submit.nice_button')
        # check button disable
        if not btn.is_enabled():
            print("FAIL: test_name_integration")
        else:
            print("SUCCESS: test_name_integration")

    def test_year_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#birthday")
        element.clear()
        element.send_keys("1999")
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_8.submit.nice_button')
        # check button disable
        if not btn.is_enabled():
            print("FAIL: test_year_integration")
        else:
            print("SUCCESS: test_year_integration")

    def test_film_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.NAME, "m_act[film]")
        # check not go anywhere and is there alert?
        self.submitInput(element, "ночь")
        # expect exception
        if (URL_page_filter not in driver.current_url):
            print("FAIL: test_film_integration")

    def test_address_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.NAME, "m_act[location]")
        # check not go anywhere and is there alert?
        self.submitInput(element, "Пышма")
        # expect exception
        if (URL_page_filter not in driver.current_url):
            print("FAIL: test_address_integration")

    def submitInput(self, element, text):
        element.clear()
        element.send_keys(text)
        element.submit()

    def goBack(self):
        driver = self.driver
        driver.back()
        driver.implicitly_wait(5)
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
