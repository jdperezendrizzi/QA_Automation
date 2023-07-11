# Importaciones Modulos
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
from SRC.PageObjects.Modulos.pageConsultas import PageConsultas

sys.path.append(r"/\\")


class TCConsultas(unittest.TestCase):

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
        self.page_consultas = PageConsultas(self.driver)
        self.page_home = PageHome(self.driver)

    #@unittest.skip("testeaando")
    def test_ir_a_formulario_consulta(self):
        # Login
        usr = self.dic_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_al_formulario()

        datos = {'detalle_mensaje': 'Pruebas Automation'}
        self.page_consultas.completar_formulario_consultas(datos)

        self.assertEqual(self.page_consultas.return_mensaje_consulta_exitoso(),
                         'La solicitud fue procesada exitosamente')

    #@unittest.skip("testeaando")
    def test_ir_a_formulario_consulta_con_adjunto(self):
        # Login
        usr = self.dic_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_al_formulario()

        datos = {'detalle_mensaje': 'Pruebas Automation',
                 'adjunto': 'C:/QA_Automation/SRC/datos/Images/imagen_1.jpeg'}
        self.page_consultas.completar_formulario_consultas(datos, True)

        self.assertEqual(self.page_consultas.return_mensaje_consulta_exitoso(),
                         'La solicitud fue procesada exitosamente')
        # TODO: agregar assert que chequee el nombre del adjunto

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
