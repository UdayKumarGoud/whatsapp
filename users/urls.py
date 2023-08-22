from django.urls import path, re_path
from . import views


urlpatterns = [
    path('send_otp/', views.SendOTPMobileAPI.as_view()),
    # path('verify_otp/', views.VerifyOTPMobileAPI.as_view()),
    # path('login/', views.UserLoginAPI.as_view()),
    
    path('edit_profile/', views.UpdateUserProfile.as_view(), name='EditProfile'),
    path('profile_me/', views.UserProfileMe.as_view(), name='GetProfile'),
    path('logout/', views.LogoutView.as_view()),
    
    
    path('login/', views.user_login, name='user_login'),
]