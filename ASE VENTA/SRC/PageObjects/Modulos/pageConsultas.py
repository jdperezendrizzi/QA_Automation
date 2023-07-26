from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class PageConsultas:
    def __init__(self, my_driver):
        self.driver = my_driver

        self.select_motivo = (By.ID, "destino")
        self.input_detalle_mensaje = (By.ID, "consulta")
        # self.input_file_doc_adjunto = (By.ID, "file-0")
        self.input_file_doc_adjunto = "file-0"
        self.button_enviar_solicitud = (
            By.XPATH, "//button[@type='submit']")
        self.button_continuar_mensaje_importante = (By.XPATH, "//button[normalize-space()='Continuar']")
        self.mensaje_consulta_exitoso = (
            By.XPATH, "//p[contains(.,'La solicitud fue procesada exitosamente')]")

    def completar_formulario_consultas(self, data, with_attach=False):
        self.seleccionar_motivo_por_indice_random()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_detalle_mensaje)).send_keys(
            data['detalle_mensaje'])
        if with_attach:
            adjunto = self.driver.find_element(By.ID, self.input_file_doc_adjunto)
            adjunto.send_keys(data['adjunto'])

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_enviar_solicitud)).click()
        try:
            WebDriverWait(self.driver, 15).until_not(EC.element_to_be_clickable(self.button_enviar_solicitud))
        finally:
            try:
                WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(
                    self.button_continuar_mensaje_importante)).click()
                WebDriverWait(self.driver, 15).until_not(EC.presence_of_element_located(self.button_enviar_solicitud))
            except TE:
                WebDriverWait(self.driver, 15).until_not(EC.presence_of_element_located(self.button_enviar_solicitud))

    def return_mensaje_consulta_exitoso(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.mensaje_consulta_exitoso)).text

    def seleccionar_motivo_por_indice_random(self):
        random = randint(1, 4)
        seleccionar_motivo = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.select_motivo))
        practica = Select(seleccionar_motivo)
        practica.select_by_index(random)
