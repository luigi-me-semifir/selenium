from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

class PageDetail:
    def __init__(self, driver: WebDriver) -> None:
        """Initialise la page de détails du produit."""
        self.driver: WebDriver = driver
        # Assurez-vous que "ffPrice" est le bon sélecteur pour le titre du produit
        self.title_locator: tuple = (By.CLASS_NAME, "RizBd")

    def titre_page_detail(self) -> str:
        """Récupère et retourne le titre du produit."""
        try:
            # Attendre que le titre du produit soit visible avant de tenter de récupérer le texte
            titre_element = WebDriverWait(self.driver, 25).until(
                EC.visibility_of_element_located(self.title_locator)
            )
            titre: str = titre_element.text
            print(f"Le titre du produit est : '{titre}'")
            return titre
        except Exception as e:
            print("Erreur lors de la tentative de récupération du titre du produit.")
            # Fournir un feedback plus détaillé sur l'erreur
            raise AssertionError(f"Titre du produit introuvable. Exception: {e}") from e
