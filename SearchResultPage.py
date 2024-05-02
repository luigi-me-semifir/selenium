from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultPage:
  def __init__(self, driver):
    self.driver = driver
    self.resultat_items_locator = (By.CLASS_NAME, "item")
  
  def click_premier_item(self):
    elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.resultat_items_locator))
    if elements:
        elements[1].click()
    else:
        raise Exception("Aucun élément trouvé.")

    