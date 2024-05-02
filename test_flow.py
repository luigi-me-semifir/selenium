import unittest
from selenium import webdriver
from CookiePage import CookiePage
from HomePage import HomePage
from SearchResultPage import SearchResultPage
from PageDetail import PageDetail

class BbeTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Chrome()
    self.driver.get("https://black-book-editions.fr/")

  def test_site(self):
    cookie_validation = CookiePage(self.driver)
    cookie_validation.validation_cookies()

    home_page = HomePage(self.driver)
    home_page.recherche("Cats! La Mascarade")

    resultat_recherche = SearchResultPage(self.driver)
    resultat_recherche.click_premier_item()

    page_detail = PageDetail(self.driver)
    page_detail.titre_page_detail()



  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":
  unittest.main()