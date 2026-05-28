from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    dict={
        'name':'Usama',
        'age': 24,
        'city': 'Hirpur',
        'country': 'Pakistan',
        'hobbies': ['coding', 'gaming', 'traveling']
}
    return render(request, 'index.html',{"info": "<br>".join(f'{key}: {value}' for key, value in dict.items())})
def game(request):
    return render(request, 'index.html')

def python(request):
    return render(request, 'index.html')

