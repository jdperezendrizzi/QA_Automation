from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PagePublic:
    def __init__(self, my_driver):
        self.driver = my_driver

        # Elementos del Forma
        self.button_mi_cuenta = (By.XPATH, "//a[@href='/login-portal-actual/']")

    def ir_a_login(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_mi_cuenta)).click()
