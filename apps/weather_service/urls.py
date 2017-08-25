from django.conf.urls import url
# importing views.py so that we can attach the methods from views.py to the respective route urls.
from . import views           
urlpatterns = [
    url(r'^$', views.index)        
  ]