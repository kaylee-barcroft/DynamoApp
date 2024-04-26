from django.test import TestCase, LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Hosttest(LiveServerTestCase):
    
    def testhomepage(self):
        driver = webdriver.Chrome()
        driver.get("http://127.0.0.1:8000/")
        assert "Dynamo Coffee" in driver.title

        time.sleep(2)


class LoginFormTest(LiveServerTestCase):

    def testform(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/accounts/login/')

        time.sleep(2)

        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.ID, 'id_password')

        time.sleep(2)

        submit = driver.find_element(By.NAME, 'submit')

        user_name.send_keys('admin')
        user_password.send_keys('admin')

        submit.send_keys(Keys.RETURN)

        assert 'admin' in driver.page_source


class SingleOriginFormTest(LiveServerTestCase):
    
    def test_create_form(self):
        #login as admin
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/accounts/login/')

        time.sleep(2)

        user_name = driver.find_element(By.NAME, 'username')
        user_password = driver.find_element(By.ID, 'id_password')

        time.sleep(2)

        submit = driver.find_element(By.NAME, 'submit')

        user_name.send_keys('krbar')
        user_password.send_keys('3kitties')

        submit.send_keys(Keys.RETURN)

        driver.get("http://127.0.0.1:8000/singleorigins/")

        add_offering = driver.find_element(By.NAME, 'add_offering')
        add_offering.send_keys(Keys.RETURN)

        time.sleep(3)
        assert 'create' in driver.current_url

        farm_field = driver.find_element(By.NAME, 'farm')
        about_field = driver.find_element(By.NAME, 'about')
        roast_field = driver.find_element(By.NAME, 'roast_profile')
        available_box = driver.find_element(By.NAME, 'available')
        submit = driver.find_element(By.NAME, "submit")

        farm_field.send_keys("test field")
        about_field.send_keys("This is a test field")
        roast_field.send_keys("Berry")
        available_box.send_keys(Keys.SPACE)
        time.sleep(1)
        submit.send_keys(Keys.RETURN)
        time.sleep(2)

        #assert test field in db.sqlite3
        assert 'singleorigins' in driver.current_url # check if redirected to list view


class SingleOriginDetailViewTest(LiveServerTestCase):
    def test_detail_view(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/singleorigins/')

        view_button = driver.find_element(By.CLASS_NAME, 'card')
        view_button.send_keys(Keys.RETURN)
        time.sleep(2)
        assert '/singleorigin/' in driver.current_url