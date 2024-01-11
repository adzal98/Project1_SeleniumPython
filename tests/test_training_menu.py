import pytest
import self as self
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from utilities.BaseClass import BaseClass
from time import sleep


class TestTrainingMenu(BaseClass):

    def test_training_video(self):

        sleep(1)
        driver = self.driver
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[5]/a")).perform()
        driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/nav/ul/li[5]/ul').click()
        wait = WebDriverWait(driver, 3)
        video_error = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/main/div[3]/div[1]/div[2]/div')))
        driver.get_screenshot_as_file("videos.png")

        assert "We found" in video_error, 'Nu exista nici un videoclip incarcat in aceasta sectiune'
