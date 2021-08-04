from django.urls import path

from . import views

urlpatterns = [
    path('', views.input, name='input'),
    path("index/",views.index,name="index"),
    path("camera/",views.camera,name="camera")
]