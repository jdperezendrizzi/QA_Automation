''' credenciales
TC

'''
import inspect
import os
import sys
import time
from lib2to3.pgen2 import driver
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

from SRC.PageObjects.Modulos.pageHome import PageHome

sys.path.append(r"/\\")

# Importaciones de Page

from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageCredenciales import PageCredenciales
from selenium.webdriver.common.alert import Alert
from random import randint
# Importaciones Modulos

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import unittest
import json
import time


class TCCredenciales(unittest.TestCase):

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
        self.page_credenciales = PageCredenciales(self.driver)
        self.page_home = PageHome(self.driver)

    @unittest.skip("Ahora no")
    def test_credencial_digital_sin_foto(self):
        # Login
        usr = self.dic_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_credencial_digital()
        time.sleep(5)
        self.page_credenciales.click_detalle_credencial()
        time.sleep(5)

        archivo_descargado = 'C:/Users/Lu/Downloads/39673475.png'
        chrome_options = Options()
        chrome_options.add_argument("--download-folder=" + archivo_descargado)

        self.page_credenciales.click_descargar()
        time.sleep(10)

        archivo_descargado = 'C:/Users/Lu/Downloads/39673475.png'
        archivo_existe = os.path.exists(archivo_descargado)

        if archivo_existe:
            print("El archivo se ha descargado correctamente.")
        else:
            print("La descarga del archivo ha fallado.")


    #@unittest.skip("Ahora no")
    def test_credenciales_002(self):
        # Login
        usr = self.dic_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_credencial_digital()
        time.sleep(5)
        self.page_credenciales.click_detalle_credencial()
        time.sleep(5)
        self.page_credenciales.click_foto_credencial()
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR,
                                                  "body.modal-open:nth-child(2) ngb-modal-window.d-block.modal.fade.show:nth-child(13) div.modal-dialog.modal-dialog-centered.modal-lg div.modal-content div.modal-body div.row.justify-content-center:nth-child(1) div.col-md-8.col-lg-5.ng-star-inserted div.credential-picture > p:nth-child(2)").text,
                         'Arrastra una foto de perfil aquí')

    @unittest.skip("Ahora no")
    def test_credenciales_003(self):

        time.sleep(20)
        # self.page_object_credenciales.click_fondo_home()
        time.sleep(8)
        self.page_credenciales.click_menu_hamburgesa()
        self.page_credenciales.click_credenciales()
        self.page_credenciales.click_foto_credencial()
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, "nav-link").text, 'Arrastra una foto de perfil')

    @unittest.skip("Ahora no")
    def test_credenciales_004(self):

        time.sleep(20)
        # self.page_object_credenciales.click_fondo_home()
        time.sleep(8)
        self.page_credenciales.click_menu_hamburgesa()
        self.page_credenciales.click_credenciales()
        self.page_credenciales.click_detalle_credencial()
        self.assertEqual(self.driver.find_element(By.XPATH,
                                                  "/html/body/ngb-modal-window/div/div/app-credencial-virtual/div[2]/div/div/div/div[2]/div/button").text,
                         'DESCARGAR')

    @unittest.skip("Ahora no")
    def test_generar_token(self):
        # Login
        usr = self.dic_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        time.sleep(15)
        self.page_credenciales.click_generar_token()
        time.sleep(5)
        self.page_credenciales.select_seleccionar_asociado(1)
        time.sleep(5)
        self.page_credenciales.click_btn_generar_token()
        time.sleep(5)
        self.assertEqual(self.page_credenciales.return_volver_a_generar_token(), 'Volver a generar el Token')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
