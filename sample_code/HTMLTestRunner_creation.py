import unittest
import HTMLTestRunner
import os

from Testcase_classdecorator import SearchTest

indir = os.getcwd()

search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)

creating_test_suite = unittest.TestSuite([search_test])

outfile = open(indir + '\sample_html_report.html', "wb")

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(
    stream=outfile,
    title='Test Report',
    description='Smoke_Test'
    )

# run the suite using HTMLTestRunner
runner.run(creating_test_suite)