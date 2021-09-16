from django.shortcuts import render
from django.http import HttpResponse ,Http404
from .models import employee
from . import models

def home(request):
    employees =employee.objects.all()
    return render(request,'home.html',{'employees':employees})


def employee_detail(request,employee_id):
    try :
        employee =models.employee.objects.get(id=employee_id)

    except models.employee.DoesNotExist:
        raise Http404('Employee not found')

    return render(request,'employee_detail.html',{'employee':employee})


