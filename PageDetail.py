from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageDetail:
  def __init__(self, driver):
    self.driver = driver
    self.title = (By.CLASS_NAME, "ffPrice")

  def titre_page_detail(self):
    try:
      titre_element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.title)
      )
      titre = titre_element.text
      print("Le titre est :", titre)
      return titre
    except Exception as ex:
      print("Produit introuvable")
      raise AssertionError("Produit introuvable.") from ex
