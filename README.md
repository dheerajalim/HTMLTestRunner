# HTMLTestRunner
HTMLTestRunner is an extension to the Python standard library's unittest module. It generates easy to use HTML test reports. You might want to generate a report of all the tests executed as evidence or to distribute test results to various stakeholders.


###The example below for running the HTMTestRunner

    import unittest
    import HTMLTestRunner
    import os

    from Testcase_classdecorator import SearchTest

    indir = os.getcwd()

    search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)

    creating_test_suite = unittest.TestSuite([search_test])

    outfile = open(indir + '\html_report.html', "wb")

    # configure HTMLTestRunner options
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=outfile,
        title='Test Report',
        description='Smoke_Test'
        )

    # run the suite using HTMLTestRunner
    runner.run(creating_test_suite)
    
  
##Creation
 
     It was originally created by tungwaiyip and upgraded recently for Python 3.5.1
     by dheerajalim
    
##How it works

    Just copy the HTMLTestRunner.py in the Python/Lib directory and then you can import it and use
    
## Contributors
- Way Yip Tung - https://github.com/tungwaiyip
