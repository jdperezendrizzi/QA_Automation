from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException as NSEE
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from random import randint
from datetime import datetime
import random


class PageCredenciales:

    def __init__(self, my_driver):
        self.driver = my_driver

        #Credencialdigital
        #                                      //*[@id='main-navbar']/div/a[1]/span
        self.menu_hamburgesa = (By.XPATH, "//*[@id='main-navbar']/div/a[1]/span")
        self.div_menu_abierto = (By.XPATH, "//div[@class='side-menu left show']//div[@class='close-area']")
        self.credenciales = (By.XPATH, "/html/body/app-root/app-header/div[1]/div[3]/nav/div[4]/a")
        self.detalle_credencial = (By.XPATH, '//*[@id="swiper-credentials"]/div/div/div/div[3]/a')
        self.fondo_home = (By.XPATH, "/html/body/app-root/main/app-mis-gestiones/div/app-panel-asociados/div")
        self.detalle_credencialparcial = (By.LINK_TEXT, "Detalle")
        self.foto_credencial = (By.CSS_SELECTOR,
                                "app-root.ng-tns-c86-0:nth-child(2) main.ng-tns-c86-0.ng-trigger.ng-trigger-fadeAnimation:nth-child(2) app-credenciales.ng-star-inserted div.py-3.page-container div.container.ng-star-inserteC:nth-child(2) div.row.my-2 div.col-12 div.credentials-container.ng-star-inserted div.s-wrapper.swiper.swiper-container.swiper-container-initialized.swiper-container-horizontal.swiper-container-pointer-events div.swiper-wrapper div.credential-card.active.swiper-slide.ng-star-inserted.swiper-slide-active div.credential-card-body.text-center div.credential-picture.mx-auto > i.icon.icon-32.icon-edit-pencil.ng-star-inserted")
        self.ayuda = (By.XPATH, "/html/body/app-root/main/app-credenciales/div/app-section-tabs/div/div/div/ul/li[2]/a")
        self.button_descargar = (By.XPATH, "//button[normalize-space()='DESCARGAR']")

        #Generar token
        self.btn_generar = (By.XPATH, "//*[@id='token']/div/div/div/div/div[2]/button/span")
        self.seleccionar_asociado = (By.XPATH, "//*[@id='token']/div/div/div/div/div[1]/select")
        self.token_home = (By.XPATH,
                           "/html/body/app-root/main/app-mis-gestiones/div/app-panel-asociados/div/div[1]/app-credencial/div/div/div[1]/div/div[2]/div/a[2]")
        self.text_generar_token = (By.XPATH, "//u[normalize-space()='Volver a generar el Token']")


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
    def click_menu_hamburgesa(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.menu_hamburgesa)).click()

    def click_credenciales(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.credenciales)).click()

    def click_detalle_credencial(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.detalle_credencial)).click()

    def click_foto_credencial(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.foto_credencial)).click()

    def click_ayuda(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ayuda)).click()

    def click_fondo_home(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.fondo_home)).click()
    def click_descargar(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.button_descargar)).click()
    def click_generar_token(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.token_home)).click()

    def select_emisor_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.emisor_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_marca_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.marca_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_producto_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.producto_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_sucursal_alta(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sucursal_alta))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_grupo_afinidad(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.grupo_afinidad))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    # NACIONALIDAD
    def select_nacionalidad(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.nacionalidad))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_tipoDocu(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.tipoDocu))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def ingresar_documento(self, random):
        random = randint(10000000, 99999999)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.documento)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.documento)).send_keys(random)

    def ingresar_apellido(self, apellido):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apellido)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apellido)).send_keys(str(apellido))

    def ingresar_nombre(self, nombre):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre)).send_keys(str(nombre))

    def ingresar_cuit_cuil(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuit_cuil)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuit_cuil)).send_keys(valor)

    def select_sexo(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sexo))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def ingresar_fecha_nacimiento(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.fecha_nacimiento)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.fecha_nacimiento)).send_keys(valor)

    def ingresar_cuenta_ext(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuenta_ext)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cuenta_ext)).send_keys(valor)

    def ingresar_email(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.email)).send_keys(valor)

    def select_pais(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.pais))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_depto_prov(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.depto_prov))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def select_seleccionar_asociado(self, valor):
        select_element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.seleccionar_asociado))
        select_object = Select(select_element)
        select_object.select_by_index(valor)

    def ingresar_localidad(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.localidad)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.localidad)).send_keys(valor)

    def ingresar_calle(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.calle)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.calle)).send_keys(valor)

    def ingresar_numero(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.numero)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.numero)).send_keys(valor)

    def ingresar_CD(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.codigo_postal)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.codigo_postal)).send_keys(valor)

    def ingresar_telefono(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.telefono)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.telefono)).send_keys(valor)

    def ingresar_nombre_embozado(self, valor):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre_embozado)).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.nombre_embozado)).send_keys(valor)

    def grabar_alta(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.grabar)).click()

    def confirmar_aceptar_prenovedad(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.aceptar_prenovedad)).click()
    def click_btn_generar_token(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_generar)).click()

    def return_descargar(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.button_descargar)).text
    def return_volver_a_generar_token(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.text_generar_token)).text
