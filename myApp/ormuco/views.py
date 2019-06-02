from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return render(request, 'ormuco/form.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'ormuco/form.html', {'form': form})