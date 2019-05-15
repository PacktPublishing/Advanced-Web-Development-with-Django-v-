from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
]
