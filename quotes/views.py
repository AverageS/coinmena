from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from quotes.models import Quote
from quotes.tasks import fetch_prices


@csrf_exempt
def quotes_view(request):
    """
    View can be replaced with DRF Viewset + Serializer but i kept it as simple as possible as reqs were saying
    :param request:
    :return:
    """
    if request.method == 'GET':
        try:
            btc_usd = Quote.objects.get(ticket='btc/usd')
        except Quote.DoesNotExist:
            return JsonResponse({'error': "BTC/USD pair does not exist"}, status=404)
        return JsonResponse({'price': btc_usd.price})
    if request.method == 'POST':
        fetch_prices.delay()
        return JsonResponse({'status': 'i started collect prices'})
