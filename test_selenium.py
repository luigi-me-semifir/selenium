# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# # Initialisation du navigateur (dans cet exemple, Chrome)
# driver = webdriver.Chrome()

# # Ouvrir une URL dans le navigateur
# driver.get("https://www.example.com")

# # Cibler un élément par son ID et cliquer dessus
# element = driver.find_element(By.ID, "exampleButton")
# element.click()

# # Remplir un formulaire en ciblant un champ par son nom
# input_field = driver.find_element(By.NAME, 'username')
# # Vide le champ si déjà remplie
# input_field.clear()
# # Remplie le champ avec la valeur donnée
# input_field.send_keys('example_user')

# # Attendre 5 secondes avant de continuer
# time.sleep(5)

# # Fermer le navigateur
# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialisation du driver pour Chrome
driver = webdriver.Chrome()
driver.get("https://black-book-editions.fr/")

# Automatisation de la validation des cookies quand on arrive sur la page
driver.find_element(By.XPATH, "//*[@id=\"form-accept-cookies\"]/button[2]").click()

# Verification qu'il y a bien une barre de recherche de disponible
try:
    bar_de_recherche = driver.find_element(By.ID, "str_to_search")
    # On vide la bar de recherche si elle est pré remplie
    bar_de_recherche.clear()
    # On fait une recherche dans la bar
    bar_de_recherche.send_keys("Cats! La Mascarade")
    # On tape sur entrée
    bar_de_recherche.send_keys(Keys.ENTER)
    
    # Attente que l'element se charge avant d'effectuer l'action demandée
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id=\"produit_13024\"]/div[2]"))
    )
    # Maintenant, vous pouvez interagir avec l'élément
    price = element.text
    print(price)
except Exception as ex:
    assert print("produit introuvable")