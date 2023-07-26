import unittest
import sys
sys.path.append(r"C:\QA_Automation")
import HtmlTestRunner

# Importo los TestCase
from SRC.Test.testLogin import TCLogin
from SRC.Test.testAutorizaciones import TCAutorizaciones
from SRC.Test.testConsultas import TCConsultas
from SRC.Test.testReintegros import TCReintegros

# Crear una instancia de TestLoader
test_loader = unittest.TestLoader()

# Carga de tests específicos
test_suite = unittest.TestSuite()
test_suite.addTest(TCLogin('test_login_email'))
test_suite.addTest(TCAutorizaciones('test_autorizaciones_solicitar_practicas_fertilidad'))
test_suite.addTest(TCAutorizaciones('test_autorizaciones_solicitar_discapacidad'))
test_suite.addTest(TCConsultas('test_ir_a_formulario_consulta_con_adjunto'))


# Ejecutar la suite de pruebas con HtmlTestRunner
test_runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Test Completos", add_timestamp=False)
test_runner.run(test_suite)
