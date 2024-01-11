# https://magento.softwaretestingboard.com/

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from time import sleep


class TestAccount(BaseClass):

    def test_createacc(self):

        driver = self.driver  # Am importat functia driver din conftest
        driver.find_element(By.XPATH, "/html/body/div[2]/header/div[1]/div/ul/li[3]/a").click()
        first_name = ("Jhon", "Katana", "Jack")
        last_name = ("Jhon", "Alisson", "Alex")
        for first in first_name:

            driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[1]/div/input").clear()
            driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[1]/div/input").send_keys(first)

            for last in last_name:
                driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[2]/div/input").clear()
                driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/form/fieldset[1]/div[2]/div/input").send_keys(last)
            driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[1]/div/input").clear()
            mail = "test@gmail.com"
            driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[1]/div/input").send_keys(mail)

            try:
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/input").clear()
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[3]/div/input").clear()
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/input").send_keys("test")
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[3]/div/input").send_keys("test")
                sleep(1)
                pass_strength = driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/div[2]/div/span").text
                if "Weak" in pass_strength:
                    pass

            finally:
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/input").clear()
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[3]/div/input").clear()
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/input").send_keys("Test1234@")
                driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[3]/div/input").send_keys("Test1234@")
                sleep(1)
                pass_strength = driver.find_element(By.XPATH,"/html/body/div[2]/main/div[3]/div/form/fieldset[2]/div[2]/div/div[2]/div/span").text

                if "Strong" in pass_strength:
                    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/form/div/div[1]/button").click()
                    sleep(1)
                    exist = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/div/div/div").text

                    if "already" in exist:
                        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

                        for letter in letters:
                            letters = "".join(letter)
                            mail = mail[0:4] + letter + "gmail.com"
                        break

            account_created = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[2]/div[2]/div/div/div").text

            assert "There is already an account" in account_created, 'We tried all varies and an account was created with good remarks'
            # Contul a fost creat cu succes


    def test_loggin(self, wrong_passw = 'qwerty', mail = 'python.testing@test.com', good_passw = 'Test1234@'):
        global input_passw, loggin_button
        driver = self.driver
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/header/div[1]/div/ul/li[2]/a').click()
            input_email = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[2]/div/input')
            input_email.send_keys(mail)
            input_passw = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[3]/div/input')
            input_passw.send_keys(wrong_passw)
            loggin_button = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[4]/div[1]/button/span')
            loggin_button.click()
            sleep(1)
            loggin_error = driver.find_element(By.XPATH, '/html/body/div[2]/main/div[2]/div[2]/div/div/div')
            wait = WebDriverWait(driver, 5)
            wait.until(EC.text_to_be_present_in_element(By.XPATH, loggin_error), 'inorrect')
            # se testeaza logarea cu o parola veche/gresita

        except:
            driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[3]/div/input').send_keys(good_passw)
            driver.find_element(By.XPATH, '/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[4]/div[1]/button/span').click()
            print('e-Mail-ul si parola sunt corecte !')

