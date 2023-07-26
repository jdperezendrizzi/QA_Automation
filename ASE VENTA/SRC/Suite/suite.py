import unittest
import sys
sys.path.append(r"C:\QA_Automation")
import HtmlTestRunner

# Importo los TestCase
from SRC.Test.testLogin import TCLogin
from SRC.Test.testAutorizaciones import TCAutorizaciones
from SRC.Test.testFacturacion import TCFacturacion
from SRC.Test.testConsultas import TCConsultas
from SRC.Test.testReintegros import TCReintegros
from SRC.Test.testBeneficios import TCBeneficios
#from SRC.Test.testVitality import TCVitality
from SRC.Test.testCredenciales import TCCredenciales
#from SRC.Test.testMora import TCMora
from SRC.Test.testToken import TCToken
from SRC.Test.testDatos import TCDatos

# Crea una instancia de TestLoader
test_loader = unittest.TestLoader()

# Carga las clases de pruebas en la suite
test_suite = unittest.TestSuite()
test_suite.addTests(test_loader.loadTestsFromTestCase(TCLogin))
test_suite.addTests(test_loader.loadTestsFromTestCase(TCAutorizaciones))
test_suite.addTests(test_loader.loadTestsFromTestCase(TCDatos))
test_suite.addTests(test_loader.loadTestsFromTestCase(TCFacturacion))
test_suite.addTests(test_loader.loadTestsFromTestCase(TCConsultas))
test_suite.addTests(test_loader.loadTestsFromTestCase(TCReintegros))
test_suite.addTests(test_loader.loadTestsFromTestCase(TCBeneficios))
test_suite.addTests(test_loader.loadTestsFromTestCase(TCCredenciales))


# Ejecuta la suite de pruebas
test_runner = unittest.TextTestRunner()
# test_runner.run(test_suite)
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Test Completos", add_timestamp=False).run(test_suite)
