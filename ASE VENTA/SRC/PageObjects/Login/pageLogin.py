import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class PageLogin:
    def __init__(self, my_driver):
        self.driver = my_driver

        # Elementos del Forma
        self.link_mi_cuenta = (By.XPATH, "//a[@href='/login-portal-actual/']")
        self.button_asociado = (By.XPATH, "//button[contains(text(),'Asociado')]")
        self.button_responsable_pago = (By.XPATH, "//button[contains(text(),'Responsable de Pago')]")

        self.button_ingreso_dni = (By.XPATH, "//button[normalize-space()='Ingresá con tu documento']")
        self.button_ingreso_mail = (By.XPATH, "//button[normalize-space()='Ingresá con tu email']")

        self.input_mail = (By.XPATH, "//input[@id='email']")
        self.input_pass = (By.ID, "password")
        self.button_login = (By.XPATH, "//button[normalize-space()='LOGIN']")
        self.text_ingresando = (By.XPATH, "//span[contains(text(),'Ingresando..')]")

        self.input_dni = (By.ID, "nrodoc")
        self.input_pass = (By.XPATH, "//input[@name='password']")
        self.select_tipo_doc = (By.ID, "tipodoc")

        self.select_tipo_doc_resp_pago = (By.XPATH, "//select[@name='fres_tipdoc']")
        self.input_dni_resp_pago = (By.XPATH, "//input[@name='fres_nrodoc']")
        self.input_pass_resp_pago = (By.XPATH, "//input[@name='fres_pass__']")
        self.button_login_resp_pago = (By.XPATH, "//button[normalize-space()='INGRESAR']")

    def ingresar(self, usr, pwd, tipo=''):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_asociado)).click()
        if tipo == 'dni':
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_ingreso_dni)).click()
        else:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_ingreso_mail)).click()
        time.sleep(2)
        if tipo == 'dni':
            self.seleccionar_tipo_doc_dni(self.select_tipo_doc)

        if tipo == 'dni':
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_dni)).send_keys(usr)
        else:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_mail)).send_keys(usr)
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_pass)).send_keys(pwd)
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_login)).click()
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.text_ingresando))
        finally:
            WebDriverWait(self.driver, 100).until_not(EC.element_to_be_clickable(self.text_ingresando))

    def ingresar_resp_pago(self, usr, pwd):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.button_responsable_pago)).click()
        time.sleep(2)
        self.seleccionar_tipo_doc_dni(self.select_tipo_doc_resp_pago)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_dni_resp_pago)).send_keys(usr)
        time.sleep(2)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_pass_resp_pago)).send_keys(pwd)
        time.sleep(2)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_login_resp_pago)).click()
        try:
            WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(self.text_ingresando))
        finally:
            WebDriverWait(self.driver, 100).until_not(EC.element_to_be_clickable(self.text_ingresando))

    def seleccionar_tipo_doc_dni(self, elem):
        select_element = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(elem))
        tipo_doc = Select(select_element)
        tipo_doc.select_by_index(0)

