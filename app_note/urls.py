from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # NOTE APP
    path('add_note/', views.add_note, name='add_note'),
    path('note_detail/<int:pk>', views.note_detail, name='note_detail'),
    path('note_edit/<int:pk>', views.note_edit, name='note_edit'),
    path('note_delete/<int:pk>', views.note_delete, name='note_delete'),

    # NOTE APP LOGIN
    path('user_login/', views.loginPage, name='login'),
    path('user_register/', views.registerPage, name='register'),
    path('user_logout/', views.logoutUser, name='logout'),

]
