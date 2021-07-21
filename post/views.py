from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post':post})

def search(request):
    posts = Post.objects.all()
    
    q = request.POST.get('q', '').replace(" ", "") # get 두번째 인자: 없으면 none가져와서 오류 줄임
    if q:
        results = posts.filter(title__icontains=q)
        return render(request, 'home.html', {'results':results})
    else:
        data = 1 # 검색어 없을 경우
        return render(request, 'home.html', {'data':data, 'posts':posts})

# def new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit = False)
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('home')
#     else:
#         form = PostForm()
#         return render(request, 'new.html', {'form':form})




