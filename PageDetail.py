from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageDetail:
    def __init__(self, driver):
        self.driver = driver
        # Assurez-vous que "ffPrice" est le bon sélecteur pour le titre du produit
        self.title_locator = (By.CLASS_NAME, "RizBd")

    def titre_page_detail(self):
        try:
            # Attendre que le titre du produit soit visible avant de tenter de récupérer le texte
            titre_element = WebDriverWait(self.driver, 25).until(
                EC.visibility_of_element_located(self.title_locator)
            )
            titre = titre_element.text
            print(f"Le titre du produit est : '{titre}'")
            return titre
        except Exception as e:
            print("Erreur lors de la tentative de récupération du titre du produit.")
            # Fournir un feedback plus détaillé sur l'erreur
            raise AssertionError(f"Titre du produit introuvable. Exception: {e}") from e
