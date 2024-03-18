from django.contrib import admin
from django.urls import path, include
from demo.views import CustomLoginView, CustomLogoutView, list_items

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('items/', list_items, name='items'),
]