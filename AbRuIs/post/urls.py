from django.urls import path
from .views import home, BlogDetailView

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='detail'),
]