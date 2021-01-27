from django.conf.urls import url
from DRF_DSL import views

urlpatterns = [ 
	  url(r'^api/university$', views.university_list),
	 
  ]