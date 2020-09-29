from django.urls import path
from . import views
urlpatterns = [
    path('', views.BbHomepage, name='BbHomepage'),
    path('profile/', views.BbProfile, name='BbProfile'),
    path('post/edit/<int:pk>', views.BbEditPost, name='BbEditPost'),
    path('post/edit/', views.BbEditedPost, name='BbEditedPost'),
    path('post/new/', views.BbCreatePost, name='BbCreatePost'),
    path('post/delete/<int:pk>', views.BbDeletePost, name='BbDeletePost'),
    path('post/like/<str:keys>', views.BbLikePost, name='BbLikePost'),
]































