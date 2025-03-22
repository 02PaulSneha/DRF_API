from django.shortcuts import render
from django.http import HttpResponse




def students(request):
    students= [
        {'id':1 , 'name': 'john' , 'age': 35}
    ]
    return HttpResponse(students)
