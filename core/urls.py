from django.urls import path

from core import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name='logout'),
    path('register', views.registerUser, name='register'),
    path('', views.home, name='home'),
    path('add/<str:pk>/', views.add, name='add'),
    path('addCategory', views.add_category, name='addCategory'),
    # path('addParticipant', views.add_participant, name='addParticipant'),
    path('github', views.github, name='github'),
    path('linkedin', views.linkedin, name='linkedin'),
    path('about', views.about, name='about'),
    path('delete/<str:pk>/', views.delete_course, name='delete'),
    path('addCourse', views.add_course, name='addCourse'),
    path('update/<str:pk>', views.update_course, name='update')
]
