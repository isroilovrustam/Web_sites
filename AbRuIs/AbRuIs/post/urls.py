from django.urls import path
from .views import home, detail, BlogListView, MalumotListView, postlar

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', detail, name='detail'),
    path('#Post', BlogListView.as_view(), name='post'),
    path('malumot/', MalumotListView.as_view(), name='info'),
    path('postlar/', postlar, name='postlar'),
]
