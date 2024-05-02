from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class HomePage:
    def __init__(self, driver: WebDriver) -> None:
        """Initialise la page d'accueil."""
        self.driver: WebDriver = driver
        # Identifiant de la barre de recherche
        self.bar_de_recherche_locator: tuple = (By.ID, "str_to_search")

    def recherche(self, texte_recherche: str) -> None:
        """Effectue une recherche en utilisant le texte spécifié."""
        try:
            # Attendre que la barre de recherche soit visible avant de continuer
            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.bar_de_recherche_locator)
            )
            # Effacer tout texte existant dans la barre de recherche
            element.clear()
            # Entrer le texte de recherche et simuler la pression de la touche 'Entrée'
            element.send_keys(texte_recherche + Keys.ENTER)
            print(f"Recherche effectuée pour : '{texte_recherche}'")
        except Exception as e:
            print(f"Erreur lors de la recherche avec le texte : '{texte_recherche}' : {e}")
            # Relance une exception pour notifier que l'opération de recherche a échoué
            raise Exception("La recherche a échoué") from e
