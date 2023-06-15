import sys
import HtmlTestRunner

# Importaciones de Page
from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageHome import PageHome
from SRC.PageObjects.Modulos.pageBeneficios import PageBeneficios
from SRC.PageObjects.Modulos.pageToken import PageToken
from SRC.PageObjects.Modulos.pageCredenciales import PageCredenciales


# Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time

sys.path.append(r"/\\")


class TCBeneficios(unittest.TestCase):

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
        self.page_beneficios = PageBeneficios(self.driver)

        self.driver.implicitly_wait(5)

    def test_beneficios(self):
            # Login
            usr = self.diccionario_usuario["UserEmail"]
            self.page_public.ir_a_login()
            self.login.ingresar(usr["email"], usr["clave"])

            self.page_home.ir_a_beneficios()
            time.sleep(10)
            self.page_beneficios.filtrar_por_nombre("infancia")
            time.sleep(5)
            self.page_beneficios.filtrar_por_categoria()
            time.sleep(5)
            self.page_beneficios.filtrar_por_provincia()

            self.assertEqual(self.page_beneficios.return_sin_resultados(), "Su búsqueda no produjo resultados")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))

