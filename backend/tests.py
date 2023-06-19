from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase


class FileViewSetTests(APITestCase):

    def test_file_list_get(self):
        url = reverse('file-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_create_post(self):
        url = reverse('file-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_file_retrieve_get(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_update_put(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.put(url, data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_partial_update_patch(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.patch(url, data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_destroy_delete(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
from django.urls import reverse

from rest_framework import status

from rest_framework.test import APITestCase


class FileViewSetTests(APITestCase):

    def test_file_list_get(self):
        url = reverse('file-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_create_post(self):
        url = reverse('file-list')
        response = self.client.post(url, data={})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_file_retrieve_get(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_update_put(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.put(url, data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_partial_update_patch(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.patch(url, data={})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_file_destroy_delete(self):
        url = reverse('file-detail', kwargs={'pk': None})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
