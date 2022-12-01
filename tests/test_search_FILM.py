import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait

URL_page_search = 'index.php'
URL_page_filter = 'https://www.kinopoisk.ru/s/'
URL_captcha = 'showcaptcha'


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Edge()

    def test_film_empty(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#find_film")
        element.clear()
        #check button disable
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_18.submit.nice_button')
        if btn.is_enabled():
            print("FAIL: test_film_empty")
        else:
            print("SUCCESS: test_film_empty")

    def test_film_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        # все верно находит
        text_correct = ["a", "или как", "когда?", "@%&*!"]
        for text in text_correct:
            element = driver.find_element(By.CSS_SELECTOR, "input#find_film")
            self.submitInput(element, text)
            # expect no exception
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_film_correct, text=", text)
            # go back
            self.goBack()


    def test_year_empty(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#year")
        element.clear()
        #check button disable
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_18.submit.nice_button')
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
            element = driver.find_element(By.CSS_SELECTOR, "input#year")
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
            element = driver.find_element(By.CSS_SELECTOR, "input#year")
            self.submitInput(element, text)
            # expect exception
            if (URL_page_filter not in driver.current_url):
                print("FAIL: test_year_wrong, text=", text)
            # go back
            self.goBack()

    def test_actor_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_correct = ["a", "фон триер", "фон-триер"]
        # установка главного поля
        for text in text_correct:
            element = driver.find_element(By.NAME, "m_act[actor]")
            self.submitInput(element, text)
            # expect no exception
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_actor_correct, text=", text)
            # go back
            self.goBack()

    def test_actor_wrong(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_wrong = ["питт, нортон", "брэд#$", "112"]
        # установка главного поля
        for text in text_wrong:
            element = driver.find_element(By.NAME, "m_act[actor]")
            self.submitInput(element, text)
            # expect exception
            if (URL_page_filter not in driver.current_url):
                print("FAIL: test_actor_wrong, text=", text)
            # go back
            self.goBack()

    def test_creators_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_correct = ["a", "фон триер", "фон-триер"]
        # установка главного поля
        for text in text_correct:
            element = driver.find_element(By.NAME, "m_act[cast]")
            self.submitInput(element, text)
            # expect no exception
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_creators_correct, text=", text)
            # go back
            self.goBack()

    def test_creators_wrong(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_wrong = ["питт, нортон", "брэд#$", "112"]
        # установка главного поля
        for text in text_wrong:
            element = driver.find_element(By.NAME, "m_act[cast]")
            self.submitInput(element, text)
            # expect exception
            if (URL_page_filter not in driver.current_url):
                print("FAIL: test_creators_wrong, text=", text)
            # go back
            self.goBack()

    def test_money_mln_correct(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_correct = ["1000", "1.5"]
        #установка главного поля
        for text in text_correct:
            element = driver.find_element(By.NAME, "m_act[box]")
            select1 =Select(driver.find_element(By.CLASS_NAME, "text.el_14"))
            select1.select_by_index(1)
            select2 = Select(driver.find_element(By.CLASS_NAME, "text.el_16"))
            select2.select_by_index(1)
            self.submitInput(element, text)
            # expect no exception
            if (URL_page_search not in driver.current_url):
                print("FAIL: test_money_mln_correct, text=", text)
  #          alert = wait.until(EC.visibility_of_element_located(By.CLASS_NAME, "ui_notice_container"))
            self.goBack()

        #wait = WebDriverWait(driver, 10)

    def test_money_mln_wrong(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        text_wrong = ["-1000", "ааа", "1*2#"]
        # установка главного поля
        for text in text_wrong:
            element = driver.find_element(By.NAME, "m_act[box]")
            select1 = Select(driver.find_element(By.CLASS_NAME, "text.el_14"))
            select1.select_by_index(1)
            select2 = Select(driver.find_element(By.CLASS_NAME, "text.el_16"))
            select2.select_by_index(1)
            self.submitInput(element, text)
            # expect exception
            if (URL_page_filter not in driver.current_url):
                print("FAIL: test_money_mln_wrong, text=", text)
            # go back
            self.goBack()

    ### INTEGRATION

    def test_film_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#find_film")
        element.clear()
        element.send_keys("кино")
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_18.submit.nice_button')
        # check button disable
        if not btn.is_enabled():
            print("FAIL: test_film_integration")
        else:
            print("SUCCESS: test_film_integration")

    def test_year_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.CSS_SELECTOR, "input#year")
        element.clear()
        element.send_keys("1999")
        driver.implicitly_wait(2)
        btn = driver.find_element(By.CLASS_NAME, 'el_18.submit.nice_button')
        # check button disable
        if not btn.is_enabled():
            print("FAIL: test_year_integration")
        else:
            print("SUCCESS: test_year_integration")

    def test_actor_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.NAME, "m_act[actor]")
        self.submitInput(element, "брэд")
        # expect exception
        if (URL_page_filter not in driver.current_url):
            print("FAIL: test_actor_integration")

    def test_creator_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.NAME, "m_act[cast]")
        self.submitInput(element, "ларс")
        # expect exception
        if (URL_page_filter not in driver.current_url):
            print("FAIL: test_creators_integration")

    def test_money_mln_integration(self):
        driver = self.driver
        driver.get("https://www.kinopoisk.ru/s/")
        if URL_captcha in driver.current_url:
            driver.implicitly_wait(10000)
        element = driver.find_element(By.NAME, "m_act[box]")
        select1 = Select(driver.find_element(By.CLASS_NAME, "text.el_14"))
        select1.select_by_index(1)
        select2 = Select(driver.find_element(By.CLASS_NAME, "text.el_16"))
        select2.select_by_index(1)
        self.submitInput(element, "1000")
        # expect exception
        if (URL_page_filter not in driver.current_url):
            print("FAIL: test_money_mln_integration")

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
