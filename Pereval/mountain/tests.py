from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Pereval, Users, Coords, Level, Images
# Create your tests here.


class TestURL(TestCase):
    def test_mainpage(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_sumbitdata(self):
        response = self.client.get('/submitData/')
        self.assertEqual(response.status_code, 200)



class TestPerevals(TestCase):
    def test_create_perevals_success(self):
        client = APIClient()
        url = '/sumbitData/'
        data = {
            'beauty_title': 'Название топонима',
            'title': 'Название перевала',
            "other_titles": "больше текста",
            'connect': 'Связь',
            'level': {
                'summer': '1B',
                'autumn': '2A',
                'winter': '3B',
                'spring': '4A',
            },
            'user': {
                'fam': 'Иванов',
                'name': 'Иван',
                'otc': 'Иванович',
                'email': 'ivan@example.com',
                'phone': 1234567890,
            },
            'coord': {
                'latitude': 55.12345,
                'longitude': 37.54321,
                'height': 100,
            },
            "images": [{"title": "Восхождение на Белуху через перевал Делоне",
                        "image": "https://avatars.mds.yandex.net/i?id=a888b186bc0ad309c4ec76e8004d5182712da87e-3163703-images-thumbs&n=13"},
                       {"title": "Взгляд новичка или Белуха в марте",
                        "image": "http://altai-photo.ru/_pu/1/81926227.jpg"}]
        }

        response = client.post(url, data, format='json')
        assert response.status_code== status.HTTP_200_OK
        assert response.data['status'] == status.HTTP_200_OK
        assert response.data['message'] == 'Успех'
        assert response.data['id'] is not None

    def test_create_perevals_invalid_data(self):
        client = APIClient()
        url = '/submitData/'
        data = {
            'beauty_title': 'Название топонима',
            'title': 'Название перевала',
        }
        
        response = client.post(url, data, format='json')
        assert response.data['status'] == status.HTTP_400_BAD_REQUEST
        assert response.data['message'] == 'Некорректный запрос'
        assert response.data['od'] is None