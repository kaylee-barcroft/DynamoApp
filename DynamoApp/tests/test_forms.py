from django.test import TestCase
from DynamoApp.forms import SingleOriginForm, SubscriptionForm, CreateUserForm

class SingleOriginFormTestCase(TestCase):

    def test_valid_so_form(self):
        data = {'farm': 'testFarm', 'about': 'about the farm', 'roast_profile': 'smoky', 'available': True}
        form = SingleOriginForm(data=data)
        self.assertTrue(form.is_valid)


    def test_missing_about_invalid(self):
        data = {'farm': 'testFarm', 'about': '', 'roast_profile': 'smoky', 'available': True}
        form = SingleOriginForm(data=data)
        self.assertFalse(form.is_valid()) and self.assertIn('about', form.errors)

