from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title ="Pizza", price= 20, inventory = 10)
        self.assertEqual(item, "Pizza : 20")
        
        