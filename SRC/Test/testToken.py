''' TOKEN
TC
'''
import inspect
import sys
import time
from random import randint, random
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import HtmlTestRunner
import sys
import time
from random import randint, random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.color import Color
import HtmlTestRunner

sys.path.append(r"/\\")

# Importaciones de Page

from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageToken import PageToken
from SRC.PageObjects.Modulos.pageCredenciales import PageCredenciales
from selenium.webdriver.common.alert import Alert
from random import randint
# Importaciones Modulos

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import unittest
import json
import time


class TCToken(unittest.TestCase):

    def setUp(self):
        # Carga de JSONS
        with open(r"C:/AUTOMATION-WEB-MEDIFE/SRC/datos/Config.Json") as ambiente:
            self.ambiente_webtest = json.loads(ambiente.read())

        with open(r"C:/AUTOMATION-WEB-MEDIFE/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"C:/AUTOMATION-WEB-MEDIFE/SRC/datos/User.Json") as usuario:
            self.dic_usuario = json.loads(usuario.read())

        # Config del driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # --headless #--start-maximized
        options.add_argument("incognito")  # --headless #--start-maximized
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.ambiente_webtest["ambiente"][0])

        # Config de Pages

        self.page_public = PagePublic(self.driver)
        self.login = PageLogin(self.driver)
        self.page_object_token = PageToken(self.driver)
        self.page_object_credenciales = PageCredenciales(self.driver)

    def test_token_001(self):
        # Login
        usr = self.dic_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        time.sleep(15)
        self.page_object_token.click_generar_token()
        time.sleep(5)
        self.page_object_token.select_seleccionar_asociado(1)
        time.sleep(5)
        self.page_object_token.click_btn_generar_token()
        time.sleep(5)
        self.assertEqual(self.page_object_token.return_volver_a_generar_token(), 'Volver a generar el Token')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
