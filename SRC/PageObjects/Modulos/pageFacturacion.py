import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from SRC.Frames import Frame


class PageFacturacion:
    def __init__(self, my_driver):

        self.driver = my_driver

        self.frame = Frame(self.driver)

        self.frame_consultas= (By.XPATH, "//iframe[@class='ng-star-inserted']")
        self.link_diskette = (By.XPATH, "//tbody/tr[1]/td[1]/a[1]")  # '//*[@id="consulta"]/app-iframe/div/iframe')  # NO funciona- FRAME

        # Pagos
        self.link_pagar = (By.XPATH, '/html/body/div[1]/div[2]/div/form/table/tbody[1]/tr/th/a')  # NO funciona- FRAME
        self.select_tarjeta = (By.NAME, "tarjeta")
        self.select_cuotas = (By.NAME, "CUOTAS")
        self.button_aceptar = (By.XPATH, '')
        self.text_disculpe = (By.XPATH, '/html/body/div/table/tbody/tr/td/b/font')

        #Debito Automatico
        self.frame_debito = (By.XPATH, "//*[@id='debito']/app-iframe/div/iframe")
        self.input_nombre = (By.XPATH, "//input[@name='nombre']")
        self.select_documento = (By.NAME, "tipodoc")
        self.input_documento = (By.XPATH, "/html/body/div[1]/div/div/form/p[2]/input")
        self.select_adherir_tarjeta = (By.NAME, "tipodebito")
        self.select_tipo_tarjeta = (By.NAME, "tarjeta")
        self.input_numero_tarjeta = (By.NAME, "nrotarjeta")
        self.select_mes_vencimiento = (By.NAME, "mes_vto")
        self.select_anio_vencimiento = (By.NAME, "anio_vto")
        self.input_banco = (By.NAME, "banco")
        self.link_enviar = (By.XPATH, "/html/body/div[1]/div/div/form/p[12]/a[1]")
        self.texto_adhesion_confirmada = (By.XPATH, "//h3[normalize-space()='Adhesión al débito automático']")

    def click_diskette(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.frame_consultas))
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(self.link_diskette)).click()

    def click_pagar(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.link_pagar)).click() #No funciona link aceptar- FRAME

    def seleccionar_tarjeta_por_valor_visible(self, texto_tarjeta):
        seleccionar_tarjeta = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_tarjeta))
        pago = Select(seleccionar_tarjeta)
        pago.select_by_visible_text(texto_tarjeta)

    def seleccionar_cuota_por_indice_random(self):
        random = randint(0, 11)
        seleccionar_cuota = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_cuotas))
        cuota = Select(seleccionar_cuota)
        cuota.select_by_index(random)

    def click_aceptar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_aceptar)).click() #No funciona Link Aceptar- FRAME

    def return_disculpe(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_disculpe)).text

    def completar_nombre(self, nombre):
        self.driver.switch_to.frame(self.driver.find_element(*self.frame_debito))
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_nombre)).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_nombre)).send_keys(
            nombre)
    def seleccionar_documento_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_documento))
        documento = Select(select_element)
        documento.select_by_index(index)
    def completar_documento (self, documento):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_documento)).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_documento)).send_keys(documento)
    def seleccionar_tarjeta_por_indice(self, credito):
        select_adherir = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_adherir_tarjeta))
        adherir = Select(select_adherir)
        adherir.select_by_index(credito)

    def seleccionar_tipo_tarjeta_por_indice(self, visa):
        select_tipo = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.select_tipo_tarjeta))
        tipo_tarjeta = Select(select_tipo)
        tipo_tarjeta.select_by_index(visa)

    def completar_numero_tarjeta(self, numero):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_numero_tarjeta)).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_numero_tarjeta)).send_keys(
            numero)

    def seleccionar_mes_por_indice(self, mes):
        element_mes = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_mes_vencimiento))
        select_mes = Select(element_mes)
        select_mes.select_by_index(mes) #por indice no lo agarra, usar random

    def seleccionar_mes_por_indice_random(self):
        random = randint(1, 12)
        select_mes = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_mes_vencimiento))
        mes = Select(select_mes)
        mes.select_by_index(random)

    def seleccionar_anio_por_indice(self, anio):
        select_anio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_anio_vencimiento))
        anio = Select(select_anio)
        anio.select_by_index(anio) #usar random

    def seleccionar_anio_por_indice_random(self):
        random = randint(1, 8)
        select_anio = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_anio_vencimiento))
        anio = Select(select_anio)
        anio.select_by_index(random)
    def completar_banco(self, banco):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_banco)).click()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.input_banco)).send_keys(
            banco)
    def click_enviar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_enviar)).click()

    def return_adhesion_debito_automatico(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.texto_adhesion_confirmada)).text


    def xxxx(self):
        return 0

    def yyyy(self):
        return 0
