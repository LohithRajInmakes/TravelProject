from . import views
from django.urls import path

urlpatterns = [
path('', views.demo,name='demo'),
# path('add/',views.addition,name="addition"),
# path('abort/',views.abort,name='abort'),
# path('close/',views.close,name='close')
]