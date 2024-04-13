from django.test import TestCase
from selenium import webdriver

# Create your tests here.

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.quit()