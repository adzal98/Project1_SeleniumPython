import pytest
import self as self
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from time import sleep
import numpy as np
from selenium.webdriver.support.color import Color


class TestWomenTops(BaseClass):


    def test_tops_jackets(self):

        driver = self.driver

        sleep(1)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/a")).perform()
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/a")).perform()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/ul/li[1]/a').click()
        sleep(1)
        women_jackets = driver.find_elements(By.XPATH, '//div/strong[1]/a')
        jackets = []
        for jacket in women_jackets:
            jackets.append(jacket.text)
        jackets = "\n".join(jackets)
        print(f'All jackets for women in stock are:{jackets}')

    def test_tops_jackets_check_size(self):
        driver = self.driver
        sleep(1)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/a")).perform()
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/a")).perform()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/ul/li[1]/a').click()
        sleep(1)

        women_jackets = driver.find_elements(By.XPATH, '//div/strong[1]/a')
        jackets_sizes = {}
        jackets_list = []
        chunked_jackets = []
        chunk_size = 1

        for jacket in women_jackets:
            jackets_list.append(jacket.text)

        for i in range(0, len(jackets_list), chunk_size):
            chunk = jackets_list[i:i + chunk_size]
            chunked_jackets.append(chunk)
            jackets_sizes['jackets'] = chunked_jackets

        women_sizes = driver.find_elements(By.XPATH, '//div[3]/div[1]/div[1]')
        sizes_list = []
        all_sizes = ['XS,S,M,L,XL']

        for size in women_sizes:
            sizes_list.append(size.text)

        remove_elements = ['\n', 'P', 'r', 'o', 'd', 'u', 'c', 't', 's', 'p', 'C', 'a', 'e', ' ', 'm', '', 'Compare Products']
        for elements in remove_elements:
            while elements in sizes_list:
                sizes_list.remove(elements)

        sizes_list = [element.replace('\n', ',') for element in sizes_list]

        chunked_sizes = []
        for i in range(0, len(sizes_list), chunk_size):
            chunk = sizes_list[i:i + chunk_size]
            chunked_sizes.append(chunk)
            jackets_sizes['sizes'] = chunked_sizes


        for i in range(len(jackets_sizes['sizes'])):
            jackets_sizes['products'] = [sizes + jackets for sizes, jackets in zip(jackets_sizes['sizes'], jackets_sizes['jackets'])]

        for sublist in jackets_sizes['sizes']:
            assert all(size in sublist for size in all_sizes), f"Not all sizes {all_sizes} are present in {sublist}"

    def test_tops_jackets_check_colours(self):

        driver = self.driver
        sleep(1)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/a")).perform()
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/a")).perform()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/ul/li[1]/a').click()
        sleep(1)

        n = 48
        for color in range(0, 2):
            driver.refresh()
            n += 1
            test_color = driver.find_element(By.CSS_SELECTOR, f"body > div:nth-child(5) > main:nth-child(4) > div:nth-child(4) > div:nth-child(1) > div:nth-child(4) > ol:nth-child(1) > li:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > div:nth-child({n})")
            test_color.click()
            # wait = WebDriverWait(driver, 10)
            # wait.until(EC.visibility_of(colors))
            sleep(3.5)
            # colors = driver.find_element(By.XPATH,'/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img')
            # take_color = colors.value_of_css_property('color')
            take_color = Color.from_string(driver.find_element(By.XPATH,'/html/body/div[2]/main/div[3]/div[1]/div[3]/ol/li[1]/div/a/span/span/img').value_of_css_property('background-color'))
            print(take_color)

