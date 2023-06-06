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


class PageAutorizaciones:

    def __init__(self, my_driver):
        self.driver = my_driver

        # solicitar
        self.button_salud_mental = (By.XPATH, "//p[contains(text(),'Salud mental')]")
        self.card_salud_mental = (By.XPATH, "//*[@id='solicitar']/div[2]/div[2]/div[1]/div/div")
        self.link_inicio_tratamiento = (By.XPATH, "//a[contains(text(),'Inicio o Continuidad de Tratamiento')]")
        self.button_aceptar = (By.XPATH, "//button[contains(text(),'Aceptar')]")
        self.button_iniciar_autorizacion = (By.XPATH, "//button[contains(text(),'INICIAR AUTORIZACIÓN')]")
        self.select_practica = (By.NAME, "practica")
        self.select_integrante = (By.ID, "integrante")
        self.input_fecha_orden_medica = (By.ID, "FECHA_ORDEN_MEDICA")
        self.input_cantidad_sesiones = (By.ID, "CANTIDAD_SESIONES")
        self.input_email_asociado = (By.ID, "EMAIL_ASOCIADO")
        self.button_enviar_solicitud = (By.CSS_SELECTOR, "button[type='submit']")
        self.text_comprobante_autorizacion = (By.XPATH, "//p[contains(text(),'Comprobante de Solicitud de autorización')]")
        self.spinner_practica_seleccionada = (By.XPATH, "//*[@id='solicitar']/div[2]/div/div[3]")
        self.spinner_solicitud_enviada = (By.XPATH, "//div[@class='spinner ng-star-inserted']")

        # consultar
        self.link_ver_detalle= (By.XPATH, '//*[@id="consultas"]/div[2]/app-autorizaciones-listado/div/div/table/tbody/tr[1]/td[6]/a/u')
        self.text_detalle_de_autorizacion= (By.XPATH, '//*[@id="autorizaciones-modal-detalle"]/div/div[1]/p')

    def ir_a_generar_autorizacion_salud_mental(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_salud_mental)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_inicio_tratamiento)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_aceptar)).click()

    def iniciar_autorizacion_salud_mental(self, indice):
        self.seleccionar_practica_por_indice(indice)

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_iniciar_autorizacion)).click()

    def enviar_solicitud2(self, autorizacion):

        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_integrante))
        integrante = Select(select_element)
        integrante.select_by_visible_text('EDGAR OSCAR LOPEZ')
        #self.seleccionar_integrante(autorizacion['indice_integrante'])
        self.ingresar_fecha_orden_medica(autorizacion['dias_atras'])

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_cantidad_sesiones)).send_keys(autorizacion['cantidad'])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_asociado)).send_keys(autorizacion['email'])

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_enviar_solicitud)).click()


    def click_salud_mental(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_salud_mental)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_salud_mental)).click()


    def click_inicio_tratamiento(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_inicio_tratamiento)).click()

    def click_aceptar(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_aceptar)).click()

    def seleccionar_practica_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_practica))
        practica = Select(select_element)
        practica.select_by_index(index)

    def seleccionar_practica_por_valor_visible(self, texto_practica):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_practica))
        practica = Select(select_element)
        practica.select_by_visible_text(texto_practica)

    def seleccionar_practica_por_indice_random(self):
        random = randint(1, 4)
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_practica))
        practica = Select(select_element)
        practica.select_by_index(random)

    def click_iniciar_autorizacion(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.button_iniciar_autorizacion)).click()

    def seleccionar_integrante(self, indice):
            select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_integrante))
            integrante = Select(select_element)
            time.sleep(5)
            try:
                integrante.select_by_index(indice)
            except NSEE:
                time.sleep(3)
                '''REPORTAR: Se pone un time.sleep() porque hay un "error" este combo no se comporta como los demas dinamicos. 
                            Deberia estar disabled hasta que carga los integrantes como combo practica'''
                integrante.select_by_index(indice)

    def ingresar_fecha_orden_medica(self, diasAtras):
        ahora = datetime.now()
        fecha = ahora - timedelta(days=diasAtras)
        fecha_sin_hora = fecha.strftime("%d/%m/%Y") # 23/02/2023
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_fecha_orden_medica)).send_keys(fecha_sin_hora)

    def ingresar_cant_sesiones(self, cantidad):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_cantidad_sesiones)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_cantidad_sesiones)).send_keys(cantidad)

    def ingresar_email_asociado(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_asociado)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_asociado)).send_keys(email)

    def enviar_solicitud(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_enviar_solicitud)).click()
        # Espera a que la solicitud haya sido enviada
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.spinner_solicitud_enviada))
        finally:
            WebDriverWait(self.driver, 30).until_not(EC.element_to_be_clickable(self.spinner_solicitud_enviada))

    def return_comprob_solic_autorizacion(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_comprobante_autorizacion)).text

    def click_ver_detalle(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_ver_detalle)).click()

    def return_detalle_de_autorizacion(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_detalle_de_autorizacion)).text
