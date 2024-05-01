from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from DynamoApp.models import SingleOrigin, Plan

class ViewsTestCase(TestCase):

    def setUp(self):
        # test user
        self.user = User.objects.create(username='testUser', password='test')

        # test single origin
        self.singleorigin = SingleOrigin.objects.create(
            farm = "Test Farm",
            about = "This is a test farm.",
            roast_profile = "Smoky",
            available = True
        )

        # test plan
        self.plan = Plan.objects.create(
            name = "Testpresso",
            price = 19.99,
            description = "Espresso",
        )


    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DynamoApp/index.html')


    def test_create_single_origin_view(self):
        client = Client()
        # Test the path
        response = client.get(reverse('create-single-origin'))
        #self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'DynamoApp/single_origin_form.html')

        # Test POST request
        data = {'farm': 'testFarm', 'about': 'about the farm', 'roast_profile': 'smoky', 'available': True}
        response = client.post(reverse('create-single-origin', data=data))
        self.assertEqual(response.status_code, 302) # Expecting a redirect after successful form submission

        # Check if the single origin was actually created
        single_origin_count = SingleOrigin.objects.count()
        self.assertEqual(single_origin_count, 2) # assuming one was created in setUp()


    def test_create_single_origin_invalid_form(self):
        client = Client()
        response = client.post(reverse('create-single-origin'), {}) # Empty form
        #self.assertEqual(response.status_code, 200) # Expecting the form to be re-rendered
        self.assertContains(response, "This field is required") # Expecting form errors to pop up