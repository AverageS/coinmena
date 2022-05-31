import requests
from celery import shared_task
from quotes.models import Quote
from coinmena.settings import ALPHAVANTAGE_API_KEY

@shared_task
def fetch_prices():
    params = {
        'function': 'CURRENCY_EXCHANGE_RATE',
        'from_currency': 'BTC',
        'to_currency': 'USD',
        'apikey': ALPHAVANTAGE_API_KEY
    }
    url = 'https://www.alphavantage.co/query'
    r = requests.get(url, params=params, timeout=10)
    data = r.json()
    price = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
    btc_usd, _ = Quote.objects.get_or_create(ticket='btc/usd')
    btc_usd.price = price
    btc_usd.save()