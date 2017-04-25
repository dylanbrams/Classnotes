from django.test import TestCase
from KilnData import KilnDataLogic
from KilnData import models

# Create your tests here.
class DataLogicTest(TestCase):
    def test_add_update_kiln(self):
        kiln_data_dict = {
            'kiln_id' : '',
            'kiln_name': 'Test'
        }
        KilnDataLogic.add_modify_kiln_data(kiln_data_dict)
        self.assertGreater(models.Kiln.objects.filter(kiln_name= 'Test').count(), 0)
