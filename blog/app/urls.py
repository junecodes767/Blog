from django.urls import path
from app.views import Nature_post

urlpatterns = [
    path('<slug:slug>/',Nature_post.as_view(),name='pageview')
]
