from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            print(f"Error in list view: {str(e)}")
            return Response({"error": str(e)}, status=500)

class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        messages.success(self.request, 'Post deleted successfully!')
        return super().form_valid(form)
