from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blogs, name="blogs"),
    path('blogs/<int:pk>', blogDetail, name="blog-detail"),
]
