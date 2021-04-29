from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.
from django.urls import reverse
from .views import index

class lab(TestCase):
    def test_lab_view_status_code(self):
        url = reverse('_index_')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

