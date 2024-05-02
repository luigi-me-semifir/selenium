import unittest
from selenium import webdriver
from CookiePage import CookiePage  # Importation de la classe CookiePage depuis le module CookiePage
from HomePage import HomePage  # Importation de la classe HomePage depuis le module HomePage
from SearchResultPage import SearchResultPage  # Importation de la classe SearchResultPage depuis le module SearchResultPage
from PageDetail import PageDetail  # Importation de la classe PageDetail depuis le module PageDetail

class BbeTest(unittest.TestCase):
    def setUp(self) -> None:
        """Configurer l'environnement avant chaque test."""
        # Initialisation du pilote Chrome et navigation vers le site web
        self.driver: webdriver.Chrome = webdriver.Chrome()
        self.driver.get("https://black-book-editions.fr/")
        # Création des instances de chaque page utilisée dans le test
        self.cookie_page: CookiePage = CookiePage(self.driver)  # Instance de la page des cookies
        self.home_page: HomePage = HomePage(self.driver)  # Instance de la page d'accueil
        self.search_result_page: SearchResultPage = SearchResultPage(self.driver)  # Instance de la page de résultats de recherche
        self.page_detail: PageDetail = PageDetail(self.driver)  # Instance de la page de détails du produit

    def test_complete_flow(self) -> None:
        """Exécuter le flux de test complet."""
        try:
            # Accepter les cookies
            self.cookie_page.validation_cookies()  # Appel à la méthode de validation des cookies
            print("Cookies acceptés.")

            # Faire une recherche
            self.home_page.recherche("Cats! La Mascarade")  # Appel à la méthode de recherche avec le terme spécifié
            print("Recherche effectuée pour 'Cats! La Mascarade'.")

            # Cliquer sur le premier résultat
            self.search_result_page.click_premier_item()  # Appel à la méthode pour cliquer sur le premier résultat
            print("Premier résultat de recherche cliqué.")

            # Vérifier le détail du produit
            title: str = self.page_detail.titre_page_detail()  # Appel à la méthode pour obtenir le titre de la page de détails
            self.assertIn("Cats!, la Mascarade - Écran de la MJ", title)  # Validation du titre attendu
            print(f"Titre vérifié et trouvé : {title}")
        except Exception as e:
            print(f"Erreur lors de l'exécution du test : {e}")
            raise

    def tearDown(self) -> None:
        """Nettoyer l'environnement après chaque test."""
        # Fermer le navigateur après chaque test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
