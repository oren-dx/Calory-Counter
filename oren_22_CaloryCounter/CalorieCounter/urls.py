from django.urls import *
from .views import *

urlpatterns = [
    path('',register,name='register'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),
    
    path('dashboard/',dashboard,name='dashboard'),
    path('profile-page/',profile_page,name='profile_page'),
    path('update-profile/',update_profile,name='update_profile'),
    
    path('consumed-calories-list/',consumed_calories_list,name='consumed_calories_list'),
    path('add-calorie/',add_calorie,name='add_calorie'),
    path('update-calorie/<str:id>/',update_calorie,name='update_calorie'),
    path('delete-calorie/<str:id>/',delete_calorie,name='delete_calorie'),
    
]
