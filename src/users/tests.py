from django.test import TestCase
from .models import User
# Create your tests here.

class UserModelTest(TestCase):
    def setUpTestData():
        User.objects.create(id='1',username='ciccio100',email='ciccioemail@libero.it')

    def username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 100)

