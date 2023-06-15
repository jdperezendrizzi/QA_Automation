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

        #discapacidad
        self.button_discapacidad = (By.XPATH, "//*[@id='solicitar']/div[2]/div[2]/div[2]/div/div/div")
        self.card_discapacidad = (By.XPATH, "//div[@class='col-sm-4 col-lg pb-3 pb-lg-0 item ng-star-inserted active']//div[@class='card']")
        self.button_autorizacion_documentacion = (By. XPATH, "//a[normalize-space()='Actualización documentación']")
        self.select_practica_discapacidad = (By.ID, "practica")
        self.button_iniciar_autorizacion_discapacidad= (By.XPATH, "//button[normalize-space()='INICIAR AUTORIZACIÓN']")
        self.select_integrante_discapacidad= (By.ID, "integrante")
        self.input_tel_asociado = (By.ID, "TELEFONO_ASOCIADO")
        self.input_email_rehabil = (By.ID, "EMAIL_ASOCIADO")
        self.input_nombre_prescriptor = (By.ID, "NOMBRE_PRESCRIPTOR")
        self.input_telefono_prescriptor = (By.ID, "CONTACTO_PRESCRIPTOR")
        self.input_documentacion_rehabil = (By.ID, "file-1159")

        #practicas medicas
        self.button_practicas_med = (By.XPATH, "//p[normalize-space()='Prácticas médicas']")
        self.card_practicas_med = (By.XPATH, "//div[@class='col-sm-4 col-lg pb-3 pb-lg-0 item ng-star-inserted active']//div[@class='card-body']")
        self.button_kinesiologia = (By.XPATH, "//a[normalize-space()='Kinesiología']")
        self.select_practica_kinesio = (By.NAME, "practica")
        self.button_iniciar_autorizacion = (By.XPATH, "//button[normalize-space()='INICIAR AUTORIZACIÓN']")
        self.select_integrante = (By.ID, "integrante")
        self.input_fecha_RPG = (By.ID, "FECHA_ORDEN_MEDICA")
        self.input_email_RPG = (By.ID, "EMAIL_ASOCIADO")
        self.input_adjuntar_orden_RPG= (By.XPATH, "//input[@id='file-448']")
        self.button_enviar_solicitud_RPG = (By.XPATH, "//button[@type='submit']")
        self.text_comprobante_RPG = (By.XPATH, "//p[@class='h4 mb-4']")

        #internacion
        self.button_internacion = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[4]/div/div/div/p')
        self.card_internacion = (By.XPATH, "//div[@class='col-sm-4 col-lg pb-3 pb-lg-0 item ng-star-inserted active']//div[@class='card-body']")
        self.button_internacion_conmat = (By.XPATH, "//a[normalize-space()='Internación con materiales']")
        self.button_aceptar_internac = (By.XPATH, "//button[normalize-space()='Aceptar']")
        self.input_institucion = (By.ID, "LUGAR_INTERNACION")
        self.input_tel_contacto = (By.ID, "TELEFONO_CONTACTO")

        #diabetes
        self.card_diabetes = (By.XPATH, "//div[@class='col-sm-4 col-lg pb-3 pb-lg-0 item ng-star-inserted active']//div[@class='card']")
        self.button_diabetes = (By.XPATH, "//p[normalize-space()='Diabetes']")
        self.button_insumos_diabetes = (By. XPATH, "//a[normalize-space()='Insumos diabetes']")
        self.input_tel_contact_asoc = (By.ID, "TEL_CONTACTO_ASOC")
        self.input_orden_diabetes = (By.ID, "file-960")
        self.input_laboratorio_diabe = (By.ID, "file-963")
        self.input_monitoreo_gluc = (By.ID, "file-962")
        self.input_justificativo = (By.ID, "file-961")

        #medicacion
        self.card_medicacion = (By.XPATH, "//div[@class='col-sm-4 col-lg pb-3 pb-lg-0 item ng-star-inserted active']//div[@class='card']")
        self.button_medicacion = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[7]/div/div/div/p')
        self.button_vacunas = (By.XPATH, "//a[normalize-space()='Vacunas']")
        self.input_orden_vacunas = (By.ID, "file-1017")
        self.input_justif_vacunas = (By.ID, "file-1018")

        #salud sexual
        self.card_salud_sexual = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[8]/div')
        self.button_salud_sexual = (By.XPATH, "//p[normalize-space()='Salud sexual integral']")
        self.button_plan_materno = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[8]/div/div/ul/a[1]')
        self.input_certificado_pren = (By.ID, "file-142")

        #traslados
        self.card_traslados =(By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[10]/div')
        self.button_traslados = (By.XPATH, "//p[normalize-space()='Traslados programados']")
        self.button_traslados_programados = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[10]/div/div/ul/a')

        #insumos
        self.card_insumos =(By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[11]/div')
        self.button_insumos = (By.XPATH, "//p[normalize-space()='Insumos']")
        self.button_descartables = (By.XPATH, "(//a[normalize-space()='Descartables'])[1]")

        #bariatrica
        self.card_bariatrica = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[12]/div')
        self.button_bariatrica1 = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[12]/div/div/div/p')
        self.button_bariatrica = (By.XPATH, "//a[normalize-space()='Bariátrica']")
        self.input_fecha_ciru = (By.ID, "FECHA_CIRUGIA")
        self.input_institucion_cirugia = (By.ID, "INSTITUCION")
        self.input_orden_bar = (By.ID, "file-1819")
        self.input_carpeta = (By.ID, "file-1820")
        self.input_lab_bar = (By.ID, "file-1821")
        self.input_VEDA = (By.ID, "file-1822")
        self.input_biopsia = (By.ID, "file-1827")
        self.input_rx = (By.ID, "file-1824")
        self.input_ecocard = (By.ID, "file-1825")
        self.input_espiro = (By.ID, "file-1826")
        self.input_polisom = (By.ID, "file-1823")

        #ortesis
        self.card_ortesis = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[13]/div')
        self.button_ortesis = (By.XPATH, "//p[normalize-space()='Órtesis']")
        self.button_otras_ortesis = (By.XPATH, "//a[normalize-space()='Otras órtesis']")

        #fertilidad
        self.card_fertilidad = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[14]/div')
        self.button_fertilidad = (By.XPATH, "//p[normalize-space()='Fertilidad']")
        self.button_medicacion_exc = (By.XPATH, "//a[normalize-space()='Medicacion Excedente']")

        #practicas odontologicas
        self.card_odontologicas = (By.XPATH, '//*[@id="solicitar"]/div[2]/div[2]/div[15]/div')
        self.button_odontologicas = (By.XPATH, "//p[normalize-space()='Prácticas odontológicas']")
        self.button_fisurados = (By.XPATH, "//a[normalize-space()='FLAP / Fisurados']")
        self.input_historia_clinica = (By.ID, "file-1188")


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

    def click_iniciar_autorizacion_discapacidad(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_iniciar_autorizacion_discapacidad)).click()

    def click_iniciar_autorizacion(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_iniciar_autorizacion)).click()

    def click_enviar_solicitud_RPG(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_enviar_solicitud_RPG)).click()
    def click_kinesiologia(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_kinesiologia)).click()

    def click_internacion_conmat(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_internacion_conmat)).click()

    def click_aceptar_internacion(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_aceptar_internac)).click()

    def click_insumos_diabetes(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_insumos_diabetes)).click()

    def click_vacunas(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_vacunas)).click()

    def click_plan_materno(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_plan_materno)).click()

    def click_traslados_programados(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_traslados_programados)).click()

    def click_descartables(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_descartables)).click()

    def click_bariatrica(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_bariatrica)).click()

    def click_otras_ortesis(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_otras_ortesis)).click()

    def click_medicacion_exc(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_medicacion_exc)).click()

    def click_fisurados(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_fisurados)).click()

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

    def click_discapacidad(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_discapacidad)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_discapacidad)).click()

    def click_practicas_med(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_practicas_med)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_practicas_med)).click()

    def click_internacion(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_internacion)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_internacion)).click()

    def click_diabetes(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_diabetes)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_diabetes)).click()

    def click_medicacion(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_medicacion)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_medicacion)).click()

    def click_salud_sexual(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_salud_sexual)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_salud_sexual)).click()

    def click_traslados(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_traslados)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_traslados)).click()

    def click_insumos(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_insumos)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_insumos)).click()

    def click_bariatrica_card(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_bariatrica1)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_bariatrica)).click()

    def click_ortesis(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_ortesis)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_ortesis)).click()

    def click_fertilidad(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_fertilidad)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_fertilidad)).click()

    def click_odontologicas(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_odontologicas)).click()
        except ECIE:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.card_odontologicas)).click()


    def click_autorizacion_documentacion(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_autorizacion_documentacion)).click()

    def click_aceptar_(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_aceptar)).click()

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

    def seleccionar_practica_kinesio_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_practica_kinesio))
        practica_kinesio = Select(select_element)
        practica_kinesio.select_by_index(index)

    def seleccionar_integrante(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_integrante))
        integrante_RPG = Select(select_element)
        integrante_RPG.select_by_index(index)

    def seleccionar_practica_discapacidad_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_practica_discapacidad))
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

    def seleccionar_integrante_discapacidad_por_indice(self, index):
        select_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.select_integrante_discapacidad))
        practica = Select(select_element)
        practica.select_by_index(index)

    def ingresar_fecha_orden_medica(self, diasAtras):
        ahora = datetime.now()
        fecha = ahora - timedelta(days=diasAtras)
        fecha_sin_hora = fecha.strftime("%d/%m/%Y") # 23/02/2023
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_fecha_orden_medica)).send_keys(fecha_sin_hora)

    def ingresar_fecha_cirugia(self, diasAdelante):
        ahora = datetime.now()
        fecha = ahora + timedelta(days=diasAdelante)
        fecha_sin_hora = fecha.strftime("%d/%m/%Y") # 23/02/2023
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_fecha_ciru)).send_keys(fecha_sin_hora)

    def ingresar_fecha_orden_medica_RPG(self, diasAtras):
        ahora = datetime.now()
        fecha = ahora + timedelta(days=diasAtras)
        fecha_sin_hora = fecha.strftime("%d/%m/%Y") # 23/02/2023
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_fecha_RPG)).send_keys(fecha_sin_hora)

    def ingresar_cant_sesiones(self, cantidad):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_cantidad_sesiones)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_cantidad_sesiones)).send_keys(cantidad)

    def ingresar_email_asociado(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_asociado)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_asociado)).send_keys(email)

    def ingresar_email_RPG(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_RPG)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_RPG)).send_keys(email)

    def ingresar_email_rehabil(self, email):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_rehabil)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_email_rehabil)).send_keys(email)

    def ingresar_tel_asociado(self, tel):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_asociado)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_asociado)).send_keys(tel)

    def ingresar_tel_contacto(self, tel):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_contacto)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_contacto)).send_keys(tel)

    def ingresar_tel_contact_asoc(self, tel):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_contact_asoc)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_tel_contact_asoc)).send_keys(tel)

    def ingresar_institucion(self, institucion):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_institucion)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_institucion)).send_keys(institucion)

    def ingresar_institucion_cirugia(self, institucion):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_institucion_cirugia)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_institucion_cirugia)).send_keys(institucion)

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

    def return_comprob_solic_RPG(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_comprobante_RPG)).text

    def adjuntar_documentacion_obligatoria(self, adjunto):
        documentacion_obligatoria = self.driver.find_element(*self.input_documentacion_rehabil)
        documentacion_obligatoria.send_keys(adjunto['documentacion'])

    def adjuntar_orden_RPG(self, adjunto):
        orden_medica = self.driver.find_element(*self.input_adjuntar_orden_RPG)
        orden_medica.send_keys(adjunto['orden'])

    def adjuntar_orden_diabetes(self, adjunto):
        orden_medica = self.driver.find_element(*self.input_orden_diabetes)
        orden_medica.send_keys(adjunto['orden'])

    def adjuntar_laboratorio(self, adjunto):
        laboratorio = self.driver.find_element(*self.input_laboratorio_diabe)
        laboratorio.send_keys(adjunto['orden'])

    def adjuntar_monitoreo_gluc(self, adjunto):
        monitoreo_gluc = self.driver.find_element(*self.input_monitoreo_gluc)
        monitoreo_gluc.send_keys(adjunto['orden'])

    def adjuntar_justificativo(self, adjunto):
        justificativo = self.driver.find_element(*self.input_justificativo)
        justificativo.send_keys(adjunto['orden'])

    def adjuntar_justif_vacunas(self, adjunto):
        justif_vacunas = self.driver.find_element(*self.input_justif_vacunas)
        justif_vacunas.send_keys(adjunto['orden'])

    def adjuntar_orden_vacunas(self, adjunto):
        orden_vacunas = self.driver.find_element(*self.input_orden_vacunas)
        orden_vacunas.send_keys(adjunto['orden'])

    def adjuntar_certificado_pren(self, adjunto):
        certificado_pren = self.driver.find_element(*self.input_certificado_pren)
        certificado_pren.send_keys(adjunto['orden'])

    def adjuntar_bariatrica(self, adjunto):
        orden_bar = self.driver.find_element(*self.input_orden_bar)
        orden_bar.send_keys(adjunto['orden'])
        carpeta_doc = self.driver.find_element(*self.input_carpeta)
        carpeta_doc.send_keys(adjunto['carpeta'])
        lab_bar = self.driver.find_element(*self.input_lab_bar)
        lab_bar.send_keys(adjunto['lab'])
        VEDA = self.driver.find_element(*self.input_VEDA)
        VEDA.send_keys(adjunto['veda'])
        biopsia = self.driver.find_element(*self.input_biopsia)
        biopsia.send_keys(adjunto['biopsia'])
        rx = self.driver.find_element(*self.input_rx)
        rx.send_keys(adjunto['rx'])
        ecocard = self.driver.find_element(*self.input_ecocard)
        ecocard.send_keys(adjunto['ecocard'])
        espiro = self.driver.find_element(*self.input_espiro)
        espiro.send_keys(adjunto['espiro'])
        polisom = self.driver.find_element(*self.input_polisom)
        polisom.send_keys(adjunto['polisom'])

    def adjuntar_historia_clinica(self, adjunto):
        orden_bar = self.driver.find_element(*self.input_historia_clinica)
        orden_bar.send_keys(adjunto['historia_clinica'])



