from datetime import datetime
import sys
import HtmlTestRunner

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

    @unittest.skip('no está más')
    def test_autorizaciones_solicitar_salud_mental(self):

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

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_autorizacion(), "Comprobante de Solicitud de autorización")

    @unittest.skip('No está más')
    def test_autorizaciones_solicitar_discapacidad(self): #no está terminado porque aparece cartel de que la combinacion tipo/subtipo no existe
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        self.page_autorizaciones.click_discapacidad()
        time.sleep(5)
        self.page_autorizaciones.click_autorizacion_documentacion()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_discapacidad_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion_discapacidad()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante_discapacidad_por_indice(1)
        self.page_autorizaciones.ingresar_tel_asociado(1158748332)
        self.page_autorizaciones.ingresar_email_rehabil("test@test.com")

        adjunto = {'documentacion': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}

        self.page_autorizaciones.adjuntar_documentacion_obligatoria(adjunto)

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_med(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        self.page_autorizaciones.click_practicas_med()
        time.sleep(5)
        self.page_autorizaciones.click_kinesiologia()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        time.sleep(5)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        self.page_autorizaciones.ingresar_fecha_orden_medica_RPG(60)
        time.sleep(5)
        self.page_autorizaciones.ingresar_email_RPG("test@test.com")

        adjunto = {'orden': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}
        self.page_autorizaciones.adjuntar_orden_RPG(adjunto)

        self.page_autorizaciones.click_enviar_solicitud_RPG()

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(), "Comprobante de Solicitud de autorización")

    @unittest.skip('no está más')
    def test_autorizaciones_solicitar_practicas_internacion(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        self.page_autorizaciones.click_internacion()
        time.sleep(5)
        self.page_autorizaciones.click_internacion_conmat()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_internacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        time.sleep(5)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        time.sleep(5)
        self.page_autorizaciones.ingresar_tel_contacto("1156739865")
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.ingresar_institucion("clinica")
        self.page_autorizaciones.ingresar_fecha_orden_medica(60)
        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(), "Comprobante de Solicitud de autorización")


    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_diabetes(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        self.page_autorizaciones.click_diabetes()
        self.page_autorizaciones.click_insumos_diabetes()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        time.sleep(5)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        time.sleep(5)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.ingresar_tel_contact_asoc(1158748332)

        adjunto = {'orden': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}
        self.page_autorizaciones.adjuntar_orden_diabetes(adjunto)
        self.page_autorizaciones.adjuntar_laboratorio(adjunto)
        self.page_autorizaciones.adjuntar_monitoreo_gluc(adjunto)
        self.page_autorizaciones.adjuntar_justificativo(adjunto)

        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(),
                         "Comprobante de Solicitud de autorización")


    @unittest.skip('no funciona')
    def test_autorizaciones_solicitar_practicas_medicacion(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_medicacion()
        self.page_autorizaciones.click_vacunas()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        time.sleep(5)
        self.page_autorizaciones.ingresar_tel_contact_asoc(1158748332)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        time.sleep(5)

        adjunto = {'orden': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}
        self.page_autorizaciones.adjuntar_orden_vacunas(adjunto)
        self.page_autorizaciones.adjuntar_justif_vacunas(adjunto)

        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(10)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(), "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_salud_sexual(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_salud_sexual()
        self.page_autorizaciones.click_plan_materno()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        time.sleep(5)
        self.page_autorizaciones.ingresar_tel_contact_asoc(1158748332)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        time.sleep(5)

        adjunto = {'orden': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}
        self.page_autorizaciones.adjuntar_certificado_pren(adjunto)
        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(),
                         "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_traslados(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_traslados()
        self.page_autorizaciones.click_traslados_programados()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.ingresar_fecha_orden_medica(60)
        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(), "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_insumos(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_insumos()
        self.page_autorizaciones.click_descartables()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.ingresar_tel_contacto("1156739865")
        self.page_autorizaciones.ingresar_fecha_orden_medica(60)
        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(10)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(), "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_bariatrica(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_bariatrica_card()
        self.page_autorizaciones.click_bariatrica()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        self.page_autorizaciones.ingresar_fecha_orden_medica(60)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        time.sleep(5)
        self.page_autorizaciones.ingresar_fecha_cirugia(60)
        time.sleep(5)
        self.page_autorizaciones.ingresar_institucion_cirugia("clinica")

        adjunto = {'orden': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'carpeta': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'lab': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'veda': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'biopsia': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'rx': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'ecocard': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'espiro': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg',
                   'polisom': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}
        self.page_autorizaciones.adjuntar_bariatrica(adjunto)

        time.sleep(10)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(10)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(),
                         "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_ortesis(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_ortesis()
        self.page_autorizaciones.click_otras_ortesis()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.ingresar_tel_contacto("1156739865")
        self.page_autorizaciones.ingresar_fecha_orden_medica(60)
        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(),
                         "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_fertilidad(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_fertilidad()
        self.page_autorizaciones.click_medicacion_exc()
        time.sleep(5)
        self.page_autorizaciones.click_aceptar_()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        time.sleep(5)
        self.page_autorizaciones.ingresar_fecha_orden_medica(60)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.ingresar_tel_contacto("1156739865")
        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(),
                         "Comprobante de Solicitud de autorización")

    #@unittest.skip('no es por aca cumpa')
    def test_autorizaciones_solicitar_practicas_odontologicas(self):
        usr = self.diccionario_usuario["UserEmail"]
        self.page_public.ir_a_login()
        self.login.ingresar(usr["email"], usr["clave"])

        self.page_home.ir_a_solicitar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.click_odontologicas()
        self.page_autorizaciones.click_fisurados()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_practica_kinesio_por_indice(1)
        self.page_autorizaciones.click_iniciar_autorizacion()
        time.sleep(5)
        self.page_autorizaciones.seleccionar_integrante(1)
        time.sleep(5)
        self.page_autorizaciones.ingresar_fecha_orden_medica(60)
        self.page_autorizaciones.ingresar_email_asociado("test@test.com")
        self.page_autorizaciones.ingresar_institucion("clinica")

        adjunto = {'historia_clinica': 'C:/QA_Automation/SRC/datos/Images/imagen_2.jpg'}
        self.page_autorizaciones.adjuntar_historia_clinica(adjunto)
        time.sleep(5)
        self.page_autorizaciones.click_enviar_solicitud_RPG()
        time.sleep(5)

        self.assertEqual(self.page_autorizaciones.return_comprob_solic_RPG(), "Comprobante de Solicitud de autorización")



    #@unittest.skip('no es por aca cumpa')
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
