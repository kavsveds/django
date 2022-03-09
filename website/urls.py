from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('',views.home,name='home'),
    path('heaven',views.heaven,name='heaven'),
    path('mumm',views.mumm,name='mumm'),
    path('singapore',views.singapore,name='singapore'),
    path('every',views.every,name='every'),
    path('last',views.last,name='last'),
]
