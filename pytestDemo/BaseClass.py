import inspect
import logging
'''
Base class use to hold common utilities
'''

class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.INFO)
        return logger
'''
# pytest -m "smoke" file path
#pip install allure-pytest
#pytest --alluredir=%allure_result_folder% ./tests
#allure serve %allure_result_folder%
#Clear the allure data user allure report --clean
'''
