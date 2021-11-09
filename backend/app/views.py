from django.views import View
from .models import Method
from django.http import JsonResponse

# Create your views here.
class MethodListView(View):
    def get(self, request):
        methodlist = Method.objects.all()
        return JsonResponse(list(methodlist.values()), safe=False)