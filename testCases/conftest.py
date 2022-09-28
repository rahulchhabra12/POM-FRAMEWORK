from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path=r"C:\Users\hp\Downloads\chromedriver_win32\chromedriver.exe")
    return driver

def pytest_configure(config):
    config._metadata['Project Name']='PomFramework'
    config._metadata['Module Name'] = 'customers'
    config._metadata['Tester'] = 'Rahul Chhabra'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins", None)
