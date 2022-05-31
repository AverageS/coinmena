from django.test import TestCase, Client, override_settings
from quotes.tasks import fetch_prices
from quotes.models import Quote
from unittest import mock

# Create your tests here.

def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    return MockResponse({'Realtime Currency Exchange Rate': {'5. Exchange Rate': 10}}, 200)



class QuotesTest(TestCase):

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_task(self, *args, **kwargs):
        fetch_prices()
        assert Quote.objects.all().count() == 1
        btc_usd = Quote.objects.all().first()
        assert btc_usd.ticket == 'btc/usd'
        assert btc_usd.price == 10


    def test_http_get(self):
        Quote.objects.create(ticket='btc/usd', price=10)
        client = Client()
        response = client.get('/api/v1/quotes/')
        data = response.json()
        assert data['price'] == '10.0000000000'



