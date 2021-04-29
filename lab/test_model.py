from django.test import TestCase

from .models import user_link
class user_linkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
#Set up non-modified objects used by all test
        user_link.objects.create(link_author="Ivan", link_name='innovations', link_url='https://meet.google.com/', link_views=0)

    def test_get_absolute_url(self):
        category=user_link.objects.get(id=1).self.assertEquals(user_link.get_absolute_url(),'/lab')
