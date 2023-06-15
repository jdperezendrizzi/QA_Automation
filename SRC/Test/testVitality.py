import sys
import HtmlTestRunner

# Importaciones de Page
from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageHome import PageHome
from SRC.PageObjects.Modulos.pageVitality import PageVitality
from SRC.PageObjects.Modulos.pageToken import PageToken
from SRC.PageObjects.Modulos.pageCredenciales import PageCredenciales


# Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time

sys.path.append(r"/\\")


class TCVitality(unittest.TestCase):

    def setUp(self):
        # Carga de JSONS
        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as ambiente:
            self.ambiente_webtest = json.loads(ambiente.read())

        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"C:/QA_Automation/SRC/datos/User.Json") as usuario:
            self.diccionario_usuario = json.loads(usuario.read())

        # Config del driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # --headless #--start-maximized
        options.add_argument("incognito")  # --headless #--start-maximized
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.ambiente_webtest["ambiente"][0])

        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.login = PageLogin(self.driver)
        self.page_home = PageHome(self.driver)
        self.page_token = PageToken(self.driver)
        self.page_credenciales = PageCredenciales(self.driver)
        self.page_vitality = PageVitality(self.driver)

        self.driver.implicitly_wait(5)

