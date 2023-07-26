from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class PageDatos:
    def __init__(self, my_driver):
        self.driver = my_driver

        self.label_numero_cuil = (By.XPATH, "//label[normalize-space()='NÚMERO DE CUIL']")

    def return_datos_cuil(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.label_numero_cuil)).text