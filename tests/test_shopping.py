import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from time import sleep
from selenium.webdriver import ActionChains

class TestMenus(BaseClass):

    def test_menu_woomen(self):

        driver = self.driver
        sleep(1)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/a")).perform()
        gear_tab = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul')
        list_gear_tab = []
        for item in gear_tab:
            list_gear_tab.append(item.text)
        list_gear_tab = '\n'.join(list_gear_tab)

        assert list_gear_tab in list_gear_tab, 'Nu se pot gasi subcategoriile din meniul gear'

        action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/a')).perform()
        tops = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[1]/ul')
        list_tops = []
        for items in tops:
            list_tops.append(items.text)
        list_tops = '\n'.join(list_tops)

        assert list_tops in list_tops, 'Nu se pot gasi subgategoriile din Tops'

        action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[2]')).perform()
        bottoms = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[2]/ul/li[2]/ul')
        list_bottoms = []
        for itm in bottoms:
            list_bottoms.append(itm.text)
        list_bottoms = '\n'.join(list_bottoms)

        assert list_bottoms in list_bottoms, 'Nu se pot gasi subgategoriile din Bottoms'

    def test_menu_men(self):

        driver = self.driver
        sleep(1)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[3]/a")).perform()
        men_tab = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[3]/ul')
        list_men_tab = []
        for item_men in men_tab:
            list_men_tab.append(item_men.text)
        list_men_tab = '\n'.join(list_men_tab)

        assert list_men_tab in list_men_tab, 'Nu se pot gasi subcategoriile din meniul Men'

        action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[3]/ul/li[1]/a')).perform()
        tops_men = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[3]/ul/li[1]/ul')
        list_tops_men = []
        for items_men in tops_men:
            list_tops_men.append(items_men.text)
        list_tops_men = '\n'.join(list_tops_men)

        assert list_tops_men in list_tops_men, 'Nu se pot gasi subgategoriile din Tops'

        action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[3]/ul/li[2]/a')).perform()
        bottoms_men = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[3]/ul/li[2]/ul')
        list_bottoms_men = []
        for itm_men in bottoms_men:
            list_bottoms_men.append(itm_men.text)
        list_bottoms_men = '\n'.join(list_bottoms_men)

        assert list_bottoms_men in list_bottoms_men, 'Nu se pot gasi subgategoriile din Bottoms'

    def test_menu_gear(self):

        driver = self.driver
        sleep(1)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[4]/a")).perform()
        gear_tab = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[4]/ul')
        list_gear_tab = []
        for item_gear in gear_tab:
            list_gear_tab.append(item_gear.text)
        list_gear_tab = '\n'.join(list_gear_tab)

        assert list_gear_tab in list_gear_tab, 'Nu se pot gasi subcategoriile din meniul gear'

        action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[4]/ul/li[1]/a')).perform()

        action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[4]/ul/li[2]/a')).perform()

        action.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[4]/ul/li[3]/a')).perform()

    def test_menu_training(self):

        driver = self.driver
        sleep(1)
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[5]/a")).perform()
        training_tab = driver.find_elements(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[5]/ul')
        list_training_tab = []
        for item_training in training_tab:
            list_training_tab.append(item_training.text)
        list_training_tab = '\n'.join(list_training_tab)

        assert list_training_tab in list_training_tab, 'Nu s-a gasit meniul de Training'
