from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name = "register"),
    path('login/', views.loginPage, name = "login"),
    path('logout/', views.logoutUser, name = "logout"),

    path('', views.AllBlogs, name = "blogs"),
    path('profile/', views.newuser, name = "profile"),
    path('createblogs/', views.CreateBlog_user, name = "createpost"),
    path('yourblogs/', views.YourBlogs, name = "yourblogs"),
    path('like_post/', views.like_post, name = "like blog"),
    path('dislike_post/', views.dislike_post, name = "dislike blog"),
    path('comment_post/', views.comment_post, name = "comment blog"),
    path('save_post/', views.save_post, name = "save blog"),
    path('saved_post/', views.saved_post, name = "saved blog"),
    path('delete_post/', views.delete_post, name = "delete blog"),
    path('editprofile/', views.editProfile, name = "editprofile"),
    path('liked_post/', views.liked_post, name = "liked post"),
]
