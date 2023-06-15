from selenium import webdriver
import unittest
import json
import HtmlTestRunner
import sys

# Importaciones de Page
from SRC.PageObjects.Public.pagePublic import PagePublic
from SRC.PageObjects.Login.pageLogin import PageLogin
from SRC.PageObjects.Modulos.pageHome import PageHome

sys.path.append(r"/\\")


class TCLogin(unittest.TestCase):

    def setUp(self):
        # Carga de JSONS
        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as ambiente:
            self.ambiente_webtest = json.loads(ambiente.read())

        with open(r"C:/QA_Automation/SRC/datos/Config.Json") as driver:
            self.driver_locate = json.loads(driver.read())

        with open(r"C:/QA_Automation/SRC/datos/User.Json") as usuario:
            self.dic_users = json.loads(usuario.read())

        # Config del driver
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")  # --headless #--start-maximized
        options.add_argument("incognito")  # --headless #--start-maximized
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.ambiente_webtest["ambiente"][0])

        # Config de Pages
        self.page_public = PagePublic(self.driver)
        self.page_login = PageLogin(self.driver)
        self.page_home = PageHome(self.driver)

    # @unittest.skip("tam testeando este esta ok")
    def test_login_dni(self):

        user_dni = self.dic_users["UserDni"]
        self.page_public.ir_a_login()
        self.page_login.ingresar(user_dni["dni"], user_dni["clave"], "dni")
        self.page_home.click_link_usuario_menu()
        self.assertEqual(f"Credencial Nro: {user_dni['credencial']}",
                         self.page_home.return_credencial_usuario_logueado())

    # @unittest.skip("tam testeando este esta ok")
    def test_login_email(self):
        user_email = self.dic_users["UserEmail"]
        self.page_public.ir_a_login()
        self.page_login.ingresar(user_email["email"], user_email["clave"])
        self.page_home.click_link_usuario_menu()
        self.assertEqual(f"Credencial Nro: {user_email['credencial']}",
                         self.page_home.return_credencial_usuario_logueado())

    @unittest.skip("no esta habilitado aun")
    def test_login_responsable_pago(self):
        user_email = self.dic_users["UserDni"]
        self.page_public.ir_a_login()
        self.page_login.ingresar_resp_pago(user_email["dni"], user_email["clave"])
        self.page_home.click_link_usuario_menu()
        # TODO: Hay que cambiar assert pero hasta no tener un usuario valido no sabemos como
        self.assertEqual(f"Credencial Nro: {user_email['credencial']}",
                         self.page_home.return_credencial_usuario_logueado())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reportes'))
