import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType
@pytest.fixture
def setup():
    driver=webdriver.Chrome()
    return driver
