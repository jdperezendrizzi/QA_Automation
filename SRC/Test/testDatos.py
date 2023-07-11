import time

from selenium import webdriver
import unittest
import json
import sys
import HtmlTestRunner

# Importaciones de Page
from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageHome import PageHome
from SRC.PageObjects.Modulos.pageDatos import PageDatos

sys.path.append(r"/\\")


class TCDatos(unittest.TestCase):

    def setUp(self):
        # Carga de JSONS
        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as ambiente:
            self.ambiente_webtest = json.loads(ambiente.read())

        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"C:/QA_Automation/SRC/datos/User.Json") as usuario:
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
        self.page_datos = PageDatos(self.driver)
        self.page_home = PageHome(self.driver)

    #@unittest.skip('Ahora no')
    def test_ir_a_formulario_consulta(self):
        # Login
        usr = self.dic_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_consulta_de_datos()
        time.sleep(5)

        self.assertEqual(self.page_datos.return_datos_cuil(), 'NÚMERO DE CUIL')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
