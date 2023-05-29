from django.shortcuts import render
from .models import post

def post_list(request):
    data = post.objects.all()
    return render(request, 'posts/posts.html', {'posts':data})

def post_detail(request,post_id):
    data = post.objects.get(id=post_id)
    return render(request,'posts/detail.html',{'post':data})
# Create your views here.
