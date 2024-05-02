from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver
        # Sélecteur pour les éléments de résultats de recherche
        self.resultat_items_locator = (By.CSS_SELECTOR, "div:not(.gbox) > .items .item")

    def click_premier_item(self):
        try:
            # Attendre que les éléments de résultats de recherche soient visibles
            elements = WebDriverWait(self.driver, 25).until(
                EC.visibility_of_all_elements_located(self.resultat_items_locator)
            )
            if elements and len(elements) > 1:
                # Cliquer sur le deuxième élément de la liste des résultats
                elements[1].click()
                print("Le deuxième élément de la recherche a été cliqué.")
            else:
                print("Moins de deux éléments trouvés dans les résultats de recherche.")
                raise Exception("Moins de deux éléments trouvés dans les résultats de recherche.")
        except Exception as e:
            print(f"Erreur lors de la tentative de cliquer sur le premier élément des résultats : {e}")
            # Lever une exception pour signaler l'échec de l'action
            raise Exception("Échec lors du clic sur le premier élément des résultats.") from e
