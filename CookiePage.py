from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CookiePage:
  def __init__(self, driver):
    self.driver = driver
    self.validation_cookies_bouton_locator = (By.XPATH, "//*[@id=\"form-accept-cookies\"]/button[2]")

  def validation_cookies(self):
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.validation_cookies_bouton_locator)).click()