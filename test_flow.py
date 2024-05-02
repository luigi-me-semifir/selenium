import unittest
from selenium import webdriver
from CookiePage import CookiePage
from HomePage import HomePage
from SearchResultPage import SearchResultPage
from PageDetail import PageDetail

class BbeTest(unittest.TestCase):
    def setUp(self):
        # Initialisation du pilote Chrome et navigation vers le site web
        self.driver = webdriver.Chrome()
        self.driver.get("https://black-book-editions.fr/")
        # Création des instances de chaque page utilisée dans le test
        self.cookie_page = CookiePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)
        self.page_detail = PageDetail(self.driver)

    def test_complete_flow(self):
        try:
            # Accepter les cookies
            self.cookie_page.validation_cookies()
            print("Cookies acceptés.")

            # Faire une recherche
            self.home_page.recherche("Cats! La Mascarade")
            print("Recherche effectuée pour 'Cats! La Mascarade'.")

            # Cliquer sur le premier résultat
            self.search_result_page.click_premier_item()
            print("Premier résultat de recherche cliqué.")

            # Vérifier le détail du produit
            title = self.page_detail.titre_page_detail()
            self.assertIn("Cats! La Mascarade", title)  # Validation du titre attendu
            print(f"Titre vérifié et trouvé : {title}")
        except Exception as e:
            print(f"Erreur lors de l'exécution du test : {e}")
            raise

    def tearDown(self):
        # Fermer le navigateur après chaque test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
