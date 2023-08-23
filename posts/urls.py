from django.urls import path
from django.conf import settings

from .views import homepage, post,allposts


urlpatterns= [
    
    path('', homepage, name = 'homepage'),
    path('post/<slug>/', post, name = 'post'),
    
    path('posts/', allposts, name = 'allposts'),
  
  ]