from django.shortcuts import render
from .models import post
from .forms import postForm

def post_list(request):
    data = post.objects.all()
    return render(request, 'posts/posts.html', {'posts':data})

def post_detail(request,post_id):
    data = post.objects.get(id=post_id)
    return render(request,'posts/detail.html',{'post':data})



def new_post(request):
    form = postForm()
    return render(request,'posts/new.html', {'form':form})
# Create your views here.
