from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PagePublic:
    def __init__(self, my_driver):
        self.driver = my_driver

        # Elementos del Form
        self.mi_cuenta = (By.XPATH, "/html/body/div[1]/div[1]/header/div/div[1]/div/div/div/div/div[1]/ul/li[3]/a/span")
        self.asociado = (By.XPATH,
                         "/html/body/ion-app/ng-component/ion-nav/page-principal/ion-content/div[2]/div/div/div/div/div/div[2]/div/button[1]")
        self.ingreso_mail = (By.XPATH,
                             "/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/div/div/div[1]/div/div[3]/button[2]")
        self.input_mail = (By.XPATH,
                           "/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/div/div/div[1]/div/div[3]/div[2]/form/input")
        self.input_pass = (By.XPATH,
                           "/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/div/div/div[1]/div/div[3]/div[2]/form/div[2]/input")
        self.loginButton = (By.XPATH,
                            "/html/body/ion-app/ng-component/ion-nav/page-login/ion-content/div[2]/div/div/div[1]/div/div[3]/div[2]/form/button")

        # Frame
        self.frame = (By.ID, "freMain")

    # Funcionalidad login

    def login(self, usr, pwd):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.mi_cuenta)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.asociado)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ingreso_mail)).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_mail)).send_keys(usr)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.input_pass)).send_keys(pwd)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.loginButton)).click()

    '''def switch_to_frame(self):

       self.driver.switch_to.frame(self.frame)

    '''

    def loginbutton(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.loginButton)).click()
