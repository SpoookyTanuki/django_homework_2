from django.contrib import admin
from django.urls import path, include
from calculator import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('<str:name>/', views.user_info)
]


