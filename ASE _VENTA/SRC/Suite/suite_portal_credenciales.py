#librerias
import sys
sys.path.append(r"C:\QA_Automation")
import unittest
import HtmlTestRunner

#ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
from SRC.Test import testCredenciales

#INSTANCIA DE LOADER Y SUIT

test_loader = unittest.TestLoader()
test_suite = unittest.TestSuite()

#AGREGADO DE TESTS A LA SUITE

test_suite.addTest(test_loader.loadTestsFromModule(testCredenciales))
# RUNNER Y REPORT HTML

h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Test credenciales", add_timestamp=False).run(test_suite)
