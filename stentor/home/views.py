from django.shortcuts import render
from .models import Post

# Create your views here.

def post_list(request):
     return render(request, 'home/post_list.html', {})
