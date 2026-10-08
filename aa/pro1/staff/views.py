from django.http import HttpResponse
from .models import Staff

def staff_list(request):
    staff = Staff.objects.all()
    return HttpResponse(staff)