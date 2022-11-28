from django.urls import path
from .views import registr, login_, logout, logout1


urlpatterns = [
    path('signup/', registr, name='signup'),
    path('sign-in/', login_, name='sign-in'),
    path('logout/', logout, name='logout'),
    path('logout1/', logout1, name='logout1'),
]