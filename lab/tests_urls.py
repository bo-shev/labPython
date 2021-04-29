from django.test import TestCase
from django.urls import reverse, resolve
# Create your tests here.
from django.urls import reverse

from .views import index, add_user_link, add_new_user_link

class lab(TestCase):
    def test_lab_url_resolves_lab_view(self):
        view = resolve('index/')
        self.assertEquals(view.func.view_class, index)

    def test_lab_view_status_code(self):
        url = reverse('_index_')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_userlink_url_resolves_lab_view(self):
        view = resolve('add_user_link/')
        self.assertEquals(view.func.view_class, add_user_link)

    def test_userlink_view_status_code(self):
        url = reverse('add_user_link')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_add_new_user_link_url_resolves_lab_view(self):
        view = resolve('userlink/newlink/')
        self.assertEquals(view.func.view_class, add_new_user_link)

    def test_add_new_user_link_view_status_code(self):
        url = reverse('userlink/newlink')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_addview_url_resolves_lab_view(self):
        view = resolve('addview/')
        self.assertEquals(view.func.view_class, index)

    def test_addview_link_view_status_code(self):
        url = reverse('addview/')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_allarticles_url_resolves_lab_view(self):
        view = resolve('allarticles/')
        self.assertEquals(view.func.view_class, index)

    def test_leve_comment_url_resolves_lab_view(self):
        view = resolve('leve_comment/')
        self.assertEquals(view.func.view_class, index)

    def test_addview_link_view_status_code(self):
        url = reverse('leve_comment//')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


