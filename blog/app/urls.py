from django.urls import path
from app import views

urlpatterns = [
    path('<slug:slug>/',views.post_detail,name='pageview')
]
