from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from awards import views

urlpatterns=[
    url(r'^$', views.welcome, name='welcome'),
    url(r'^new/project', views.new_project, name='new-project'),
    url(r'^projects/', views.projects, name='projects'),

]
