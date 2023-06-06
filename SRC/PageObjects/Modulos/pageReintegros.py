import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException as ECIE
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
from datetime import timedelta
import random


class PageReintegros:

    def __init__(self, my_driver):

        self.driver = my_driver
        self.by_id = By.ID

        # Consultadereintegros
        self.frame_consulta = (By.XPATH, "//iframe[@class='ng-star-inserted']")
        self.input_fecha_desde = (By.NAME, "P_FECHA_DESDE")
        self.input_fecha_hasta = (By.NAME, "P_FECHA_HASTA")
        self.button_cerrar = (By.XPATH, "//a[normalize-space()='Cerrar']")
        self.button_buscar = (By.XPATH, "//input[@value='Buscar']")
        self.texto_no_reintegros = (By.XPATH, "//td[normalize-space()='No se encontraron reintegros.']")

        #Gestionatusreintegros
        self.link_gestiona = (By.XPATH, '/html/body/app-root/main/app-reintegros/div/app-section-tabs/div/div/div/ul/li[2]/a')
        self.link_ingresa_cuestionario = (By.XPATH, "//a[normalize-space()='INGRESÁ AL FORMULARIO AQUÍ']")
        self.frame_gestiona = (By.XPATH, "//iframe[@class='ng-star-inserted']")
        self.input_tel_prefijo = (By.NAME, "telprefijo")
        self.input_tel_fijo = (By.NAME, "telfijo")
        self.input_email = (By.NAME, "email")
        self.input_domicilio_titular= (By.NAME, "domicilio_titular")
        self.input_cantidad_recibos= (By.NAME, "cant_recibos")
        self.input_monto_recibos= (By.NAME, "monto_recibos")
        self.select_adjunto_documentacion= (By.NAME, "adjunta")
        self.check_factura= (By.NAME, "factura")
        self.button_factura= (By.ID, 'adj_factura')
        self.check_orden= (By.NAME, "orden")
        self.button_orden= (By.NAME, "adj_orden")
        self.check_radiografias = (By.NAME, "radiografia")
        self.button_radiografias = (By.NAME, "adj_radiografia")
        self.check_resultados = (By.NAME, "resultados")
        self.button_resultados = (By.NAME, "adj_resultados")
        self.check_formulario_salud = (By.NAME, "formsalud")
        self.button_formulario_salud = (By.NAME, "adj_formsalud")
        self.check_formulario_odontologia= (By.NAME, "formodo")
        self.button_formulario_odontologia = (By.NAME, "adj_formodo")
        self.input_CBU = (By.NAME, "cb_cbu")
        self.input_nro_cuenta = (By.NAME, "cb_nrocta")
        self.select_tipo_cuenta = (By.NAME, "cb_tipocta")
        self.link_enviar = (By.XPATH, "//a[normalize-space()='Enviar']")
        self.texto_exito_reintegro = (By.XPATH, "//p[contains(text(),'Tu pedido de reintegro se inició con éxito. Dentro')]")


    def click_gestiona_tus_reintegros(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_gestiona)).click()
    def click_ingresa_cuestionario(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.frame_gestiona))
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.link_ingresa_cuestionario)).click()
    def completar_inputs(self, prefijo, fijo, email,domicilio, recibos, monto):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_tel_prefijo)).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_tel_prefijo)).send_keys(prefijo)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_fijo)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_fijo)).send_keys(fijo)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email)).send_keys(email)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_domicilio_titular)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_domicilio_titular)).send_keys(domicilio)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_cantidad_recibos)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_cantidad_recibos)).send_keys(recibos)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_monto_recibos)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_monto_recibos)).send_keys(monto)

    def seleccionar_adjunto_por_indice(self, si):
        select_adjunto = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_adjunto_documentacion))
        adjuntar = Select(select_adjunto)
        adjuntar.select_by_index(si)
    def adjuntar_archivos(self, adjuntos):
        if adjuntos['factura'] != '':
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.check_factura)).click()
            time.sleep(5)
            facturas = self.driver.find_element(*self.button_factura)
            facturas.send_keys(adjuntos['factura'])
        if adjuntos['ord_med']:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.check_orden)).click()
            time.sleep(5)
            self.driver.find_element(*self.button_orden).send_keys(adjuntos['ord_med'])
        if adjuntos['radio']:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.check_radiografias)).click()
            time.sleep(5)
            self.driver.find_element(*self.button_radiografias).send_keys(adjuntos['radio'])
        if adjuntos['resul_estu']:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.check_resultados)).click()
            time.sleep(5)
            self.driver.find_element(*self.button_resultados).send_keys(adjuntos['resul_estu'])
        if adjuntos['form_sad_men']:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.check_formulario_salud)).click()
            time.sleep(5)
            self.driver.find_element(*self.button_formulario_salud).send_keys(adjuntos['form_sad_men'])
        if adjuntos['form_odonto']:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.check_formulario_odontologia)).click()
            time.sleep(5)
            self.driver.find_element(*self.button_formulario_odontologia).send_keys(adjuntos['form_odonto'])

    def completar_datos_cuenta(self, cbu, numero_cuenta, CA):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_CBU)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_CBU)).send_keys(cbu)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_nro_cuenta)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_nro_cuenta)).send_keys(numero_cuenta)

        select_tipo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_tipo_cuenta))
        tipo_cuenta = Select(select_tipo)
        tipo_cuenta.select_by_index(CA)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_enviar)).click()

    def completar_fechas(self, fecha_hasta, fecha_desde):
        self.driver.switch_to.frame(self.driver.find_element(*self.frame_consulta))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_fecha_desde)).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_fecha_desde)).send_keys(fecha_hasta)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_fecha_hasta)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_fecha_hasta)).send_keys(fecha_desde)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_cerrar)).click()
        time.sleep(5)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_buscar)).click()

    def return_no_reintegros(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.texto_no_reintegros)).text

    def return_exito_reintegro(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.texto_exito_reintegro)).text












