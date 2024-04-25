from django.test import TestCase
from selenium import webdriver

# Create your tests here.

driver = webdriver.Chrome()
driver.get("127.0.0.1:8000/")
driver.get("127.0.0.1:8000/singleorigins/")
driver.quit()