from django.urls import path
from . import views, chapter

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('chapter1/', chapter.chapter1, name="chapter1"),
    path('chapter2/', chapter.chapter2, name="chapter2"),
]