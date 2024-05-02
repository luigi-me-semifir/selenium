from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
  def __init__(self, driver):
    self.driver = driver
    self.bar_de_recherche_locator = (By.ID, "str_to_search")

  def recherche(self, texte_recherche):
    element = WebDriverWait(self.driver, 10).until(
      EC.visibility_of_element_located(self.bar_de_recherche_locator)
    )
    element.clear()
    element.send_keys(texte_recherche + Keys.ENTER)
  