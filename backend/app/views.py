import json
from .functions import centradas, simpson
from django.views import View
from django.http import JsonResponse

# Create your views here.
class IntegralsMethod(View):
    def post(self, request):
        data = json.loads(request.body)
        result = simpson(data['a'], data['b'], data['n'], data['f'])
        result_dict = { 'result': result}
        data.update(result_dict)
        return JsonResponse(data, safe=False)

class DerivatesMethod(View):
    def post(self, request):
        data = json.loads(request.body)
        result = centradas(data['x'], data['delta'], data['f'])
        result_dict = { 'result': result}
        data.update(result_dict)
        return JsonResponse(data, safe=False)