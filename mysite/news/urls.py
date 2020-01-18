from django.urls import path,include
from django.views.generic import ListView, DeleteView
from news.models import Articles

urlpatterns = [
    path('',
    ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    template_name="news/posts.html")),
    path(('<int:pk>'), DeleteView.as_view(model = Articles, template_name = "news/post.html"))
]
