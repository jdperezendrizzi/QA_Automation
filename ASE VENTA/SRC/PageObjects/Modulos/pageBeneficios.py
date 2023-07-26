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


class PageBeneficios:

    def __init__(self, my_driver):

        self.driver = my_driver

        #Filtrar
        self.frame_beneficios= (By.XPATH, "//*[@id='beneficio']/app-iframe/div/iframe")
        self.input_nombre = (By.NAME, "Buscar")
        self.button_buscar = (By.ID, 'component/button/Primary/Grey/Inicial-Copy-2')
        self.span_categoria = (By.XPATH, '//*[@id="filtro-buscador-categorias-action-texto"]/p')
        self.button_alimentacion = (By.ID, "btn_1_filtros_beneficios")
        self.span_provincias =(By.XPATH, '//*[@id="texto-filtro-provincias"]/p')
        self.button_cordoba =(By.ID, 'btn_1_filtros_beneficios_provincias')
        self.texto_sinresultados_confirmado = (By.CLASS_NAME, "sin-resultados")

    def filtrar_por_nombre(self, infancia):
        self.driver.switch_to.frame(self.driver.find_element(*self.frame_beneficios))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_nombre)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.input_nombre)).send_keys(infancia)
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_buscar)).click()

    def filtrar_por_categoria(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.span_categoria)).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_alimentacion)).click()

    def filtrar_por_provincia(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.span_provincias)).click()
        time.sleep(5)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_cordoba)).click()

    def return_sin_resultados(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.texto_sinresultados_confirmado)).text



