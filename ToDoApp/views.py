from django.shortcuts import render
from django.http import HttpResponse
from .models import Tasks
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def index(request):
    return render(request, "base.html")


def add_task(Request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        task = data.get("task")

        return HttpResponse("added task")
