from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('blogs/', blogs, name="blogs"),
    path('blogs/<int:pk>', blogDetail, name="blog-detail"),
    path('contact', contact, name="contact"),
    path('portfolio', portfolio, name="portfolio"),
    path('portfolio/<int:pk>', portfolioDetail, name="portfolio-detail"),
]
