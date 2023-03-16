from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from profile_app.models import User, Subscribe
from rest_framework_simplejwt.tokens import RefreshToken


class SubscribeApiTestCase(APITestCase):
    def setUp(self):
        self.first_user = User.objects.create(
            username='user',
            email='email@.mail.ru',
            phone_num='+79283423223',
            password='vasil12345'
        )
        self.first_user.save()
        self.two_user = User.objects.create(
            username='newuser',
            email='newemail@.mail.ru',
            phone_num='+79283423423',
            password='vasil12345'
        )
        self.two_user.is_active = True
        self.two_user.save()
        self.three_user = User.objects.create(
            username='newuser123',
            email='newemai123l@mail.ru',
            phone_num='+79283426523',
            password='vasil12345'
        )
        self.three_user.save()

    def jwt_auth(self, user):
        self.token = RefreshToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION=f'JWT {self.token.access_token}')

    def get_list_subscribe(self):
        return self.client.get(reverse('list_subs', kwargs={'pk': self.first_user.id}))

    def test_create_subs(self):
        self.jwt_auth(self.three_user)
        url = reverse('add_del_subs', kwargs={'pk': self.first_user.id})
        responce = self.client.put(url, format='json')
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)

    def test_subscribe_user(self):
        self.jwt_auth(self.three_user)
        url = reverse('add_del_subs', kwargs={'pk': self.first_user.id})
        self.client.put(url, format='json')
        response = self.get_list_subscribe()
        self.assertEqual(1, len(response.json()))
        self.client.put(url, format='json')
        new_response = self.get_list_subscribe()
        self.assertEqual(0, len(new_response.json()))

    def test_del_subs(self):
        self.jwt_auth(self.three_user)
        response = self.client.put(reverse('add_del_subs', kwargs={'pk': self.first_user.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(1, len(self.get_list_subscribe().json()))
        self.jwt_auth(self.first_user)
        self.client.delete(reverse('del_subs_pk', kwargs={'pk': self.first_user.id, 'num_subs': 2}), format='json')
        self.assertEqual(0, len(self.get_list_subscribe().json()))


