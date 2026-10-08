from django.http import HttpResponse
from .models import Fee

def fee_list(request):
    fees = Fee.objects.all()
    return HttpResponse(fees)