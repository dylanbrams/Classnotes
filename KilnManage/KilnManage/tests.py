from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status

from KilnData import KilnDataLogic, models

# Create your tests here.

class DataLogicTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='su_logic_test', email='dylan@dylanbrams.com', password='this_is_a_pass')

    def test_kiln_add_logic(self):
        kiln_data_dict = {
            'kiln_id' : None,
            'kiln_name': 'TestAdd'
        }
        output_kiln = KilnDataLogic.add_modify_kiln_data(kiln_data_dict)
        self.assertEqual('TestAdd', output_kiln.kiln_name)

# REST Framework Tests.  Run initially to build test kiln data.
class KilnTests(APITestCase):

    def test_add_kiln_api(self):
        #request = factory.post('/api/kiln/', {'kiln_name':'First Kiln Test'}, format='json')
        user = User.objects.create_superuser(
            username='su_API_test', email='dylan@dylanbrams.com', password='this_is_a_passthnst12')
        self.client.force_authenticate(user)
        url = reverse('kiln-list')
        data = {'kiln_name': 'Another_kiln'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        #print (models.Kiln.objects.count())
        self.assertEqual(models.Kiln.objects.count(), 1)
        self.assertEqual(models.Kiln.objects.get().kiln_name, 'Another_kiln')
