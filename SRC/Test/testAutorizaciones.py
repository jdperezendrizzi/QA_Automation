from datetime import datetime
import sys
import HtmlTestRunner
import time
# Importaciones de Page
from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageHome import PageHome
from SRC.PageObjects.Modulos.pageToken import PageToken
from SRC.PageObjects.Modulos.pageCredenciales import PageCredenciales
from SRC.PageObjects.Modulos.pageAutorizaciones import PageAutorizaciones


# Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time

sys.path.append(r"/\\")


class TCAutorizaciones(unittest.TestCase):

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
        self.page_autorizaciones = PageAutorizaciones(self.driver)

        self.driver.implicitly_wait(5)

    @unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar(self):

        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        self.page_autorizaciones.click_salud_mental()
        self.page_autorizaciones.click_inicio_tratamiento()
        self.page_autorizaciones.click_aceptar()
        self.page_autorizaciones.seleccionar_practica_por_indice_random()
        self.page_autorizaciones.click_iniciar_autorizacion()
        self.page_autorizaciones.seleccionar_integrante(1)
        self.page_autorizaciones.ingresar_fecha_orden_medica(40)
        self.page_autorizaciones.ingresar_cant_sesiones(10)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.enviar_solicitud()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(), "Comprobante de Solicitud "
                                                                                       "de autorización")

    @unittest.skip('no es por aca cumpa')
    def test_autorizaciones_consultar(self):

        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_consultar_autorizacion()
        time.sleep(10)
        self.page_autorizaciones.click_ver_detalle()
        time.sleep(10)

        self.assertEqual(self.page_autorizaciones.return_detalle_de_autorizacion(), "Detalle de la autorización")

    def tearDown(self):
        self.driver.save_screenshot(f'error{datetime.now()}.jpg')
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
