from django.shortcuts import render
from .models import Channel
# Create your views here.

def stream(request):
    return render(request, 'viewer/stream.html', {})
