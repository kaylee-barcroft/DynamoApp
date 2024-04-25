from django.test import TestCase
from django.contrib.auth.models import User
from DynamoApp.models import SingleOrigin, Plan, Manager, Customer

class ModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to set up clean data.")
        # Create a user for testing
        self.manager = Manager.objects.create(
            managerUser = User.objects.create(
                username = "testUser",
                email = "test@user.com",
                password = "test"
            )
        )
        

        # Create a single origin
        self.singleorigin = SingleOrigin.objects.create(
            #specify the creation parameters
            farm = "Test Farm",
            about = "This is a test farm.",
            roast_profile = "Smoky",
            available = True
        )

        # Create a plan
        self.plan = Plan.objects.create(
            name = "Testpresso",
            price = 19.99,
            description = "Espresso",
            duration = 3
        )


    def test_single_origin_creation(self):
        self.assertEqual(self.singleorigin.farm, "Test Farm")
        self.assertEqual(self.singleorigin.about, "This is a test farm.")
        self.assertEqual(self.singleorigin.roast_profile, "Smoky")
        self.assertTrue(self.singleorigin.available)
        self.assertEqual(str(self.singleorigin), self.singleorigin.farm)
        


    def test_plan_creation(self):
        self.assertEqual(self.plan.name, "Testpresso")
        self.assertEqual(self.plan.price, 19.99)
        self.assertEqual(self.plan.description, "Espresso")
        self.assertEqual(self.plan.duration, 3)
        self.assertEqual(str(self.plan), self.plan.name)
        

    def test_manager_creation(self):
        self.assertEqual(self.manager.managerUser.username, "testUser")


    # example for testing get absolute url:
    # self.assertEqual(self.student.get_absolute_url(), '/student/1')