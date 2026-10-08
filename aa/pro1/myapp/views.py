from django.http import HttpResponse
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return HttpResponse(students)