# DjangoのImport
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# モデルのImport
from .models import Post

# フォームのImport
from .forms import PostForm

# 投稿一覧
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# 投稿詳細
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# 投稿作成
def post_new(request):
    if request.method == "POST":    # フォームの値を取得
        form = PostForm(request.POST)
        if form.is_valid(): # フォームの値が有効な値の場合
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:   # 初期状態は白紙で表示
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# 投稿編集
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # publish_dateを外すことでドラフトが作成できる
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})

# ドラフト投稿リスト
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

# ドラフトを投稿
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)