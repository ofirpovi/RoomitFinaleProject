from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name= 'users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/logout.html'), name='logout'),
    path('fill_info/<str:username>/', users_views.info, name='fill_info'),
    path('profile/<str:username>/', users_views.profile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name= 'users/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name= 'users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name= 'users/password_reset_complete.html'), name='password_reset_complete'),
    path('set-status/', users_views.set_status, name='set-status'),
    path('insert-in-status-form/', users_views.insert_in_status, name='insert-in-status-form'),
] + static(settings.MEDIA_URL, dcoumrnt_root=settings.MEDIA_ROOT)