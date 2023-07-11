from datetime import datetime
import sys
import HtmlTestRunner

# Importaciones de Page
from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageHome import PageHome
from SRC.PageObjects.Modulos.pageReintegros import PageReintegros
from SRC.PageObjects.Modulos.pageToken import PageToken
from SRC.PageObjects.Modulos.pageCredenciales import PageCredenciales


# Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time

sys.path.append(r"/\\")


class TCReintegros(unittest.TestCase):

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
        self.page_reintegros = PageReintegros(self.driver)

        self.driver.implicitly_wait(5)

    # @unittest.skip('Ahora no')
    def test_consulta_de_reintegros(self):
        # Login
        usr = self.diccionario_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])
        self.page_home.ir_a_reintegros()
        time.sleep(20)
        self.page_reintegros.completar_fechas("04/04/2023", "17/05/2023")
        time.sleep(10)

        self.assertEqual(self.page_reintegros.return_no_reintegros(), "No se encontraron reintegros.")

    #@unittest.skip('Ahora no')
    def test_gestion_de_reintegros(self):
        # Login
        usr = self.diccionario_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])
        self.page_home.ir_a_reintegros()
        time.sleep(10)
        self.page_reintegros.click_gestiona_tus_reintegros()
        self.page_reintegros.click_ingresa_cuestionario()
        time.sleep(10)
        self.page_reintegros.completar_inputs("011", "1539776542", "medifeapptest97@medife.com.ar", "Juana Manso 230", "3", "1345.89")
        self.page_reintegros.seleccionar_adjunto_por_indice(0)

        adjuntos = {'factura': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                    'ord_med': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                    'radio': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                    'resul_estu': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                    'form_sad_men': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                    'form_odonto': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'
                    }

        self.page_reintegros.adjuntar_archivos(adjuntos)
        time.sleep(5)
        self.page_reintegros.completar_datos_cuenta("02900230100056024123", "000402300056024123", "0")

        self.assertEqual(self.page_reintegros.return_exito_reintegro(), "Tu pedido de reintegro se inició con éxito. Dentro de las próximas 72 horas hábiles te estaremos respondiendo. ¡Muchas gracias por utilizar nuestros canales digitales! Por cualquier consulta, comunicate con nosotros al 0800 333 2700 las 24 hs")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))