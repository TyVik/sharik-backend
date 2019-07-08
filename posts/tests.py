from django.conf import settings
from django.test import TestCase
from django.urls import reverse
from django.utils.crypto import get_random_string


class PostTestCase(TestCase):
    key = get_random_string()

    def test_create(self):
        url = reverse('create_post')
        link = 'https://tyvik.ru/'

        with self.settings(POST_KEY=self.key):
            data = {'key': '', 'link': link}
            response = self.client.get(url, data)
            self.assertEqual(response.status_code, 400)
            content = response.json()
            self.assertIn('key', content.keys())

            data = {'key': settings.POST_KEY, 'link': 'bad_link'}
            response = self.client.get(url, data)
            self.assertEqual(response.status_code, 400)
            content = response.json()
            self.assertIn('link', content.keys())

            data = {'key': settings.POST_KEY, 'link': link}
            response = self.client.get(url, data)
            self.assertEqual(response.status_code, 201)
            content = response.json()
            self.assertIn('id', content.keys())
