from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Post
from .forms import PostForm, CommentForm

class PostListView(ListView):
    model = Post
    # template_name = 'post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('posts:post-detail', pk=post.pk)
        return self.render_to_response(self.get_context_data(form=form))
    

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:post-list')  # Перенаправление после успешного создания

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts:post-list') 

class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('posts:post-list') 