from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CookiePage:
    def __init__(self, driver):
        self.driver = driver
        # Xpath pour le bouton d'acceptation des cookies
        self.validation_cookies_bouton_locator = (By.XPATH, "//*[@id='form-accept-cookies']/button[2]")

    def validation_cookies(self):
        try:
            # Attendre que le bouton d'acceptation des cookies soit cliquable avant de cliquer
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.validation_cookies_bouton_locator)).click()
            print("Cookies acceptés.")
        except Exception as e:
            print(f"Erreur lors de l'acceptation des cookies: {e}")
            # Relance une exception pour notifier que l'opération a échoué
            raise Exception("L'acceptation des cookies a échoué") from e
