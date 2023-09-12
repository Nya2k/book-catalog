from django.test import TestCase, Client
from .models import Item

class modelTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
        
    def test_object_exist(self):
        name_object = Item.objects.create(name='Buku 1', amount=10, description='Ini buku 1')
        name_object_exist = Item.objects.filter(name="Buku 1").exists()
        self.assertTrue(name_object_exist)