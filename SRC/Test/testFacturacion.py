#Importaciones Modulos
from selenium import webdriver
import unittest
import json
import time
import sys

#Importaciones de Page
from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageHome import PageHome
from SRC.PageObjects.Modulos.pageFacturacion import PageFacturacion

sys.path.append(r"/\\")


class TCFacturacion (unittest.TestCase):

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
        self.page_home = PageHome(self.driver)
        self.page_facturacion = PageFacturacion(self.driver)

    #@unittest.skip("Not needed now")
    def test_facturacion_facturas(self):
        usr = self.dic_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_facturas()
        time.sleep(10)
        self.page_facturacion.click_diskette()
        time.sleep(5)
        self.assertTrue(True)

    @unittest.skip("Falta Pagos")
    def test_facturacion_pagos(self): #FALTA PAGOS
        # Login
        usr = self.dic_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        time.sleep(5)
        self.page_home.ir_a_pagar()
        time.sleep(15)
        self.page_facturacion.click_pagar()
        time.sleep(10)
        self.page_facturacion.seleccionar_tarjeta_por_valor_visible("Tarjeta de Credito VISA")
        self.page_facturacion.seleccionar_cuota_por_indice_random()
        self.page_facturacion.click_aceptar()
        time.sleep(10)

        # self.assertEqual(self.page_facturacion.return_disculpe(),
        # 'Disculpe, su operación no puede ser concluída. Por favor, vuelva a la página inicial.') #Nos da una pantalla de error en la operación

    #@unittest.skip("Not needed now")
    def test_facturacion_debito_automat_credito(self):
        # Login
        usr = self.dic_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_adhesion_debito_automatico()
        time.sleep(15)
        self.page_facturacion.completar_nombre("nombre")
        self.page_facturacion.seleccionar_documento_por_indice(0)
        self.page_facturacion.completar_documento("34922841")
        self.page_facturacion.seleccionar_tarjeta_por_indice(1)
        time.sleep(5)
        self.page_facturacion.seleccionar_cuenta_tarjeta_por_indice(0)
        self.page_facturacion.completar_numero_tarjeta("4540730050372123")
        time.sleep(5)
        self.page_facturacion.seleccionar_mes_por_indice_random()
        self.page_facturacion.seleccionar_anio_por_indice_random()
        self.page_facturacion.completar_banco("bbva")
        self.page_facturacion.click_enviar()

        self.assertEqual(self.page_facturacion.return_adhesion_debito_automatico(), "Adhesión al débito automático")

    @unittest.skip("No se realiza por error en web")
    def test_facturacion_debito_automat_cuenta(self):
        # Login
        usr = self.dic_usuario["UserEmail2"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_adhesion_debito_automatico()
        time.sleep(10)
        self.page_facturacion.completar_nombre("nombre")
        self.page_facturacion.seleccionar_documento_por_indice(0)
        self.page_facturacion.completar_documento("34922841")
        self.page_facturacion.seleccionar_tarjeta_por_indice(2)
        time.sleep(5)
        self.page_facturacion.seleccionar_cuenta_tarjeta_por_indice(0)
        self.page_facturacion.completar_cbu("0070117020000003965944")
        self.page_facturacion.completar_banco("bbva")
        self.page_facturacion.click_enviar()

        self.assertEqual(self.page_facturacion.return_adhesion_debito_automatico(), "Adhesión al débito automático")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completo")
