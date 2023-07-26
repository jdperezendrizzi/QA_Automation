import time

#import self as self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.support.ui import WebDriverWait

class PageHome:
    def __init__(self, my_driver):
        self.driver = my_driver

        self.div_menu_abierto = (By.XPATH, "//div[@class='side-menu left show']//div[@class='close-area']")
        self.menu_izquierdo = (By.XPATH, "//div[@class='side-menu-content pr-3 ng-star-inserted']")
        self.menu_derecho = (By.XPATH, "//div[@class='side-menu-content']")
        self.link_menu_derecho = (By.XPATH, '//*[@id="main-navbar"]/div/a[4]')

        self.text_credencial_usuario_menu = (By.XPATH, "//div[contains(text(),'Credencial Nro:')]")

        self.button_solicitar = (By.XPATH, "//a[@href='/portal/autorizaciones?tab=solicitar']")
        self.button_consultar = (By.XPATH, "//a[@href='/portal/autorizaciones?tab=consultas']")

        self.button_facturas = (By.CSS_SELECTOR, "body > app-root:nth-child(2) > main:nth-child(2) > app-mis-gestiones:nth-child(2) > div:nth-child(1) > app-panel-asociados:nth-child(2) > div:nth-child(1) > div:nth-child(5) > app-generic-widget:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)")
        self.button_pagar = (By.XPATH, '//a[@href="/portal/facturaciones/pagar"]')
        self.button_debito = (By.XPATH, '//*[@id="cards-container"]/div[5]/app-generic-widget/div/div/div[2]/div/div/a[2]')

        self.button_formulario_consultas = (By.XPATH, "//*[@id='cards-container']/div[6]/app-generic-widget/div")

        self.button_reintegros = (By.XPATH, "//p[normalize-space()='Reintegros']")
        self.button_beneficios = (By.XPATH, "//p[normalize-space()='Beneficios']")
        self.button_consulta_datos = (By.XPATH, '//*[@id="cards-container"]/div[4]/app-generic-widget/div/div/div[2]/div/div/a')
        self.button_credencial_digital = (By.XPATH, '//*[@id="cards-container"]/div[1]/app-credencial/div/div/div[1]/div/div[2]/div/a[1]')
    def esperar_cierre_menu_izq(self):
        no_such_elem = False
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.div_menu_abierto))
        except NSEE:
            no_such_elem = True
        except TE:
            no_such_elem = True
        finally:
            if not no_such_elem:
                WebDriverWait(self.driver, 15).until_not(EC.element_to_be_clickable(self.div_menu_abierto))

    def esperar_cambio_menu_der(self, to_open: bool):
        if to_open:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.menu_derecho))
        else:
            try:
                WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.menu_derecho))
            finally:
                WebDriverWait(self.driver, 15).until_not(EC.element_to_be_clickable(self.menu_derecho))

    def ir_a_solicitar_autorizacion(self):
        self.esperar_cierre_menu_izq()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_solicitar)).click()

    def ir_a_consultar_autorizacion(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_consultar)).click()

    def ir_a_facturas(self):
        self.esperar_cierre_menu_izq()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_facturas)).click()

    def ir_a_pagar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_pagar)).click()

    def ir_a_adhesion_debito_automatico(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_debito)).click()

    def ir_a_reintegros(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_reintegros)).click()

    def ir_al_formulario(self):
        self.esperar_cierre_menu_izq()
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.button_formulario_consultas)).click()

    def ir_a_beneficios(self):
        self.esperar_cierre_menu_izq()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_beneficios)).click()

    def ir_a_consulta_de_datos(self):
        self.esperar_cierre_menu_izq()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_consulta_datos)).click()

    def ir_a_credencial_digital(self):
        self.esperar_cierre_menu_izq()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_credencial_digital)).click()

    def click_link_usuario_menu(self):
        self.esperar_cierre_menu_izq()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.link_menu_derecho)).click()

    def return_credencial_usuario_logueado(self):
        self.esperar_cambio_menu_der(True)
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.text_credencial_usuario_menu)).text
